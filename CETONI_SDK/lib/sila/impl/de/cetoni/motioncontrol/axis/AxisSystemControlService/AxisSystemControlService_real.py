"""
________________________________________________________________________

:PROJECT: sila_cetoni

*Axis System Control Service*

:details: AxisSystemControlService:
    Provides functionality to observe and control the state of an axis system

:file:    AxisSystemControlService_real.py
:authors: Florian Meinicke

:date: (creation)          2020-12-15T07:50:56.811849
:date: (last modification) 2020-12-15T07:50:56.811849

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
import time         # used for observables
import uuid         # used for observables
import grpc         # used for type hinting only

from typing import Dict

from configparser import ConfigParser, NoSectionError, NoOptionError

# import SiLA2 library
import sila2lib.framework.SiLAFramework_pb2 as silaFW_pb2
# import SiLA errors
from impl.common.qmix_errors import SiLAFrameworkError, SiLAFrameworkErrorType, SiLAExecutionError

# import gRPC modules for this feature
from .gRPC import AxisSystemControlService_pb2 as AxisSystemControlService_pb2
# from .gRPC import AxisSystemControlService_pb2_grpc as AxisSystemControlService_pb2_grpc

# import default arguments
from .AxisSystemControlService_default_arguments import default_dict

from qmixsdk.qmixmotion import Axis, AxisSystem

# noinspection PyPep8Naming,PyUnusedLocal
class AxisSystemControlServiceReal:
    """
    Implementation of the *Axis System Control Service* in *Real* mode
        Allows to control motion systems like axis systems
    """

    def __init__(self, axis_system: AxisSystem, sila2_conf: ConfigParser):
        """
        Class initialiser.

        :param axis_system: The axis system that this feature shall operate on
        :param sila2_conf: The config of the server
        """

        self.axis_system = axis_system
        self.sila2_conf = sila2_conf

        self.axes: Dict[str, Axis] = {
            self.axis_system.get_axis_device(i).get_device_name(): self.axis_system.get_axis_device(i)
            for i in range(self.axis_system.get_axes_count())
        }

        logging.debug('Started server in mode: {mode}'.format(mode='Real'))

        self._restore_last_drive_position_counters()

    def _restore_last_drive_position_counters(self):
        """
        Reads the last drive position counters from the server's config file.
        """
        for axis_name in self.axes.keys():
            try:
                drive_pos_counter = int(self.sila2_conf[axis_name]["drive_pos_counter"])
                logging.debug("Restoring drive position counter (%d) for %s", drive_pos_counter, axis_name)
                self.axes[axis_name].restore_position_counter(drive_pos_counter)
            except NoSectionError as err:
                logging.error("No section for %s in SiLA2 config file: %s", axis_name, err)
            except (NoOptionError, KeyError) as err:
                logging.error("Cannot read config file option in %s", err)
                logging.error("No drive position counter found! Homing move needed!")

    def EnableAxisSystem(self, request, context: grpc.ServicerContext) \
            -> AxisSystemControlService_pb2.EnableAxisSystem_Responses:
        """
        Executes the unobservable command "Enable Axis System"
            Set all axes of the axis system into enabled state

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        self.axis_system.enable(True)

        return AxisSystemControlService_pb2.EnableAxisSystem_Responses()


    def DisableAxisSystem(self, request, context: grpc.ServicerContext) \
            -> AxisSystemControlService_pb2.DisableAxisSystem_Responses:
        """
        Executes the unobservable command "Disable Axis System"
            Set all axes of the axis system into disabled state

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        self.axis_system.enable(False)

        return AxisSystemControlService_pb2.DisableAxisSystem_Responses()


    def ClearFaultState(self, request, context: grpc.ServicerContext) \
            -> AxisSystemControlService_pb2.ClearFaultState_Responses:
        """
        Executes the unobservable command "Clear Axis Fault State"
            Clears the fault condition of all axes. This is some kind of error acknowledge that clears the last fault and sets the device in an error-free state.

        :param request: gRPC request containing the parameters passed:
            request.EmptyParameter (Empty Parameter): An empty parameter data type used if no parameter is required.
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: The return object defined for the command with the following fields:
            EmptyResponse (Empty Response): An empty response data type used if no response is required.
        """

        for name, axis in self.axes.items():
            logging.debug(f"Axis {name} {'is' if axis.is_in_fault_state() else 'is not'} in fault state")
            axis.clear_fault()

        return AxisSystemControlService_pb2.ClearFaultState_Responses()


    def Get_AvailableAxes(self, request, context: grpc.ServicerContext) \
            -> AxisSystemControlService_pb2.Get_AvailableAxes_Responses:
        """
        Requests the unobservable property Available Axes
            The names of the individual axes of the axis system.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            AvailableAxes (Available Axes): The names of the individual axes of the axis system.
        """

        return AxisSystemControlService_pb2.Get_AvailableAxes_Responses(
            AvailableAxes=[
                silaFW_pb2.String(value=axis_name) for axis_name in self.axes.keys()
            ]
        )

    def Subscribe_AxisSystemState(self, request, context: grpc.ServicerContext) \
            -> AxisSystemControlService_pb2.Subscribe_AxisSystemState_Responses:
        """
        Requests the observable property Axis System State
            The current state of the axis system. This is either 'Enabled' or 'Disabled'. Only if the state is 'Enabled', the axis system can move.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            AxisSystemState (Axis System State): The current state of the axis system. This is either 'Enabled' or 'Disabled'. Only if the sate is 'Enabled', the axis system can move.
        """

        while True:
            enabled = True
            for name, axis in self.axes.items():
                logging.debug(f"Axis {name} {'is' if axis.is_enabled() else 'is not'} enabled")
                enabled &= axis.is_enabled()

            logging.debug(f"Axis system {'is' if enabled else 'is not'} enabled")
            yield AxisSystemControlService_pb2.Subscribe_AxisSystemState_Responses(
                AxisSystemState=silaFW_pb2.String(value='Enabled' if enabled else 'Disabled')
            )

            time.sleep(0.5) # give client some time to catch up

    def Subscribe_AxesInFaultState(self, request, context: grpc.ServicerContext) \
            -> AxisSystemControlService_pb2.Subscribe_AxesInFaultState_Responses:
        """
        Requests the observable property Axes In Fault State
            Returns all axes of the system that are currently in fault state. The fault state of all axes can be cleared by calling ClearFaultState.

        :param request: An empty gRPC request object (properties have no parameters)
        :param context: gRPC :class:`~grpc.ServicerContext` object providing gRPC-specific information

        :returns: A response object with the following fields:
            AxesInFaultState (Axis Fault State): Returns all axes of the system that are currently in fault state. The fault state of all axes can be cleared by calling ClearFaultState.
        """

        while True:
            yield AxisSystemControlService_pb2.Subscribe_AxesInFaultState_Responses(
                AxesInFaultState=[
                    silaFW_pb2.String(value=axis_name) for axis_name, axis in self.axes.items() if axis.is_in_fault_state()
                ]
            )

            time.sleep(0.5) # give client some time to catch up