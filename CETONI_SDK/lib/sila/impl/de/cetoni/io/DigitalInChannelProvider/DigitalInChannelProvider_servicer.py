"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Digital In Channel Provider*

:details: DigitalInChannelProvider:
    Allows to control one digital in channel of an I/O module

:file:    DigitalInChannelProvider_servicer.py
:authors: Florian Meinicke

:date: (creation)          2020-12-08T14:25:47.296795
:date: (last modification) 2020-12-08T14:25:47.296795

.. note:: Code generated by sila2codegenerator 0.2.0

________________________________________________________________________

**Copyright**:
  This file is provided "AS IS" with NO WARRANTY OF ANY KIND,
  INCLUDING THE WARRANTIES OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

  For further Information see LICENSE file that comes with this distribution.
________________________________________________________________________
"""

__version__ = "0.1.0"

# import general packages
import logging
import grpc

# meta packages
from typing import Union

# import SiLA2 library
import sila2lib.framework.SiLAFramework_pb2 as silaFW_pb2
from sila2lib.error_handling.server_err import SiLAError

# import SiLA errors
from impl.common.qmix_errors import QmixSDKSiLAError, DeviceError, SiLAFrameworkError, SiLAValidationError

# import gRPC modules for this feature
from .gRPC import DigitalInChannelProvider_pb2 as DigitalInChannelProvider_pb2
from .gRPC import DigitalInChannelProvider_pb2_grpc as DigitalInChannelProvider_pb2_grpc

# import simulation and real implementation
from .DigitalInChannelProvider_simulation import DigitalInChannelProviderSimulation
from .DigitalInChannelProvider_real import DigitalInChannelProviderReal


class DigitalInChannelProvider(DigitalInChannelProvider_pb2_grpc.DigitalInChannelProviderServicer):
    """
    The SiLA 2 driver for Qmix I/O Devices
    """
    implementation: Union[DigitalInChannelProviderSimulation, DigitalInChannelProviderReal]
    simulation_mode: bool

    def __init__(self, channel_gateway, simulation_mode: bool = True):
        """
        Class initialiser.

        :param channel_gateway: The ChannelGatewayService feature that provides
                                the channels that this feature can operate on
        :param simulation_mode: Sets whether at initialisation the simulation mode is active or the real mode.
        """

        self.channel_gateway = channel_gateway
        self.simulation_mode = simulation_mode
        if simulation_mode:
            self.switch_to_simulation_mode()
        else:
            self.switch_to_real_mode()

    def _inject_implementation(self,
                               implementation: Union[DigitalInChannelProviderSimulation,
                                                     DigitalInChannelProviderReal]
                               ) -> bool:
        """
        Dependency injection of the implementation used.
            Allows to set the class used for simulation/real mode.

        :param implementation: A valid implementation of the QmixIOServicer.
        """

        self.implementation = implementation
        return True

    def switch_to_simulation_mode(self):
        """Method that will automatically be called by the server when the simulation mode is requested."""
        self.simulation_mode = True
        self._inject_implementation(DigitalInChannelProviderSimulation())

    def switch_to_real_mode(self):
        """Method that will automatically be called by the server when the real mode is requested."""
        self.simulation_mode = False
        self._inject_implementation(DigitalInChannelProviderReal(self.channel_gateway))



    def Subscribe_State(self, request, context: grpc.ServicerContext) \
            -> DigitalInChannelProvider_pb2.Subscribe_State_Responses:
        """
        Requests the observable property State
            The state of the channel.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response stream with the following fields:
            request.State (State): The state of the channel.
        """

        logging.debug(
            "Property State requested in {current_mode} mode".format(
                current_mode=('simulation' if self.simulation_mode else 'real')
            )
        )
        try:
            for value in self.implementation.Subscribe_State(request, context):
                yield value
        except (SiLAFrameworkError, DeviceError) as err:
            if isinstance(err, DeviceError):
                err = QmixSDKSiLAError(err)
            err.raise_rpc_error(context=context)
