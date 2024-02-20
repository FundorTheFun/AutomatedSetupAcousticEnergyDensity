﻿<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="23008000">
	<Property Name="NI.LV.All.SourceOnly" Type="Bool">true</Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="NI.SortType" Type="Int">3</Property>
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Examples" Type="Folder">
			<Item Name="Tektronix TBS 2000 Series Acquire Auto Setup Continuous Waveform.vi" Type="VI" URL="/&lt;instrlib&gt;/Tektronix TBS 2000 Series/Examples/Tektronix TBS 2000 Series Acquire Auto Setup Continuous Waveform.vi"/>
			<Item Name="Tektronix TBS 2000 Series Acquire Auto Setup Waveform.vi" Type="VI" URL="/&lt;instrlib&gt;/Tektronix TBS 2000 Series/Examples/Tektronix TBS 2000 Series Acquire Auto Setup Waveform.vi"/>
			<Item Name="Tektronix TBS 2000 Series Acquire Dual Channel Waveform.vi" Type="VI" URL="/&lt;instrlib&gt;/Tektronix TBS 2000 Series/Examples/Tektronix TBS 2000 Series Acquire Dual Channel Waveform.vi"/>
			<Item Name="Tektronix TBS 2000 Series Acquire Single Channel Waveform.vi" Type="VI" URL="/&lt;instrlib&gt;/Tektronix TBS 2000 Series/Examples/Tektronix TBS 2000 Series Acquire Single Channel Waveform.vi"/>
			<Item Name="Tektronix TBS 2000 Series I2C Bus Trigger.vi" Type="VI" URL="/&lt;instrlib&gt;/Tektronix TBS 2000 Series/Examples/Tektronix TBS 2000 Series I2C Bus Trigger.vi"/>
			<Item Name="Tektronix TBS 2000 Series Read Immediate Measurement.vi" Type="VI" URL="/&lt;instrlib&gt;/Tektronix TBS 2000 Series/Examples/Tektronix TBS 2000 Series Read Immediate Measurement.vi"/>
			<Item Name="Tektronix TBS 2000 Series Search CAN Bus Event.vi" Type="VI" URL="/&lt;instrlib&gt;/Tektronix TBS 2000 Series/Examples/Tektronix TBS 2000 Series Search CAN Bus Event.vi"/>
			<Item Name="Tektronix TBS 2000 Series.bin3" Type="Document" URL="/&lt;instrlib&gt;/Tektronix TBS 2000 Series/Examples/Tektronix TBS 2000 Series.bin3"/>
		</Item>
		<Item Name="Private" Type="Folder"/>
		<Item Name="Public" Type="Folder">
			<Item Name="Action-Status" Type="Folder"/>
			<Item Name="Configuration" Type="Folder">
				<Item Name="Acquisition" Type="Folder"/>
				<Item Name="Bus" Type="Folder"/>
				<Item Name="Search" Type="Folder"/>
				<Item Name="Trigger" Type="Folder"/>
			</Item>
			<Item Name="Data" Type="Folder">
				<Item Name="Low Level" Type="Folder"/>
			</Item>
			<Item Name="Utility" Type="Folder"/>
		</Item>
		<Item Name="AD2_DO_SDK.lvclass" Type="LVClass" URL="../AD2_DO_SDK_class/AD2_DO_SDK.lvclass"/>
		<Item Name="AD2_MSO_SDK.lvclass" Type="LVClass" URL="../AD2_MSO_SDK_class/AD2_MSO_SDK.lvclass"/>
		<Item Name="AD2_SDK.lvclass" Type="LVClass" URL="../AD2_SDK_class/AD2_SDK.lvclass"/>
		<Item Name="AD2_WFG_SDK.lvclass" Type="LVClass" URL="../AD2_WFG_SDK_class/AD2_WFG_SDK.lvclass"/>
		<Item Name="AFG3022B.lvclass" Type="LVClass" URL="../AFG3022B_class/AFG3022B.lvclass"/>
		<Item Name="Application.lvclass" Type="LVClass" URL="../Application_class/Application.lvclass"/>
		<Item Name="FirstStepsRead.vi" Type="VI" URL="../Peltier controller TC/TCxxxx/Examples/FirstStepsRead.vi"/>
		<Item Name="CetoniPump.lvclass" Type="LVClass" URL="../CetoniPump_class/CetoniPump.lvclass"/>
		<Item Name="DOConfigureCustomData.ctl" Type="VI" URL="../AD2_DO_SDK_class/DOConfigureCustomData.ctl"/>
		<Item Name="Main.vi" Type="VI" URL="../Main.vi"/>
		<Item Name="Main_Test.vi" Type="VI" URL="../Main_Test.vi"/>
		<Item Name="Olasdwf.lvlib" Type="Library" URL="../Olasdwf/Olasdwf.lvlib"/>
		<Item Name="TBS2000Series.lvclass" Type="LVClass" URL="../TBS2000Series_class/TBS2000Series.lvclass"/>
		<Item Name="Tektronix TBS 2000 Series.aliases" Type="Document" URL="/&lt;instrlib&gt;/Tektronix TBS 2000 Series/Tektronix TBS 2000 Series.aliases"/>
		<Item Name="Tektronix TBS 2000 Series.lvlib" Type="Library" URL="/&lt;instrlib&gt;/Tektronix TBS 2000 Series/Tektronix TBS 2000 Series.lvlib"/>
		<Item Name="TC0608.lvclass" Type="LVClass" URL="../TC0608_class/TC0608.lvclass"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="instr.lib" Type="Folder">
				<Item Name="Tektronix AFG 3000 Series.lvlib" Type="Library" URL="/&lt;instrlib&gt;/Tektronix AFG 3000 Series/Tektronix AFG 3000 Series.lvlib"/>
				<Item Name="Initialize.vi" Type="VI" URL="/&lt;instrlib&gt;/TCxxxx/Public/Initialize.vi"/>
				<Item Name="Write.vi" Type="VI" URL="/&lt;instrlib&gt;/TCxxxx/Public/Utility/Write.vi"/>
				<Item Name="Read.vi" Type="VI" URL="/&lt;instrlib&gt;/TCxxxx/Public/Utility/Read.vi"/>
				<Item Name="Close.vi" Type="VI" URL="/&lt;instrlib&gt;/TCxxxx/Public/Close.vi"/>
			</Item>
			<Item Name="vi.lib" Type="Folder">
				<Item Name="8.6CompatibleGlobalVar.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/config.llb/8.6CompatibleGlobalVar.vi"/>
				<Item Name="Application Directory.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Application Directory.vi"/>
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="Check if File or Folder Exists.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Check if File or Folder Exists.vi"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="FormatTime String.vi" Type="VI" URL="/&lt;vilib&gt;/express/express execution control/ElapsedTimeBlock.llb/FormatTime String.vi"/>
				<Item Name="General Error Handler Core CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler Core CORE.vi"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="LVRectTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVRectTypeDef.ctl"/>
				<Item Name="NI_AALBase.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALBase.lvlib"/>
				<Item Name="NI_AALPro.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALPro.lvlib"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="NI_LVConfig.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/config.llb/NI_LVConfig.lvlib"/>
				<Item Name="NI_MABase.lvlib" Type="Library" URL="/&lt;vilib&gt;/measure/NI_MABase.lvlib"/>
				<Item Name="NI_MAPro.lvlib" Type="Library" URL="/&lt;vilib&gt;/measure/NI_MAPro.lvlib"/>
				<Item Name="NI_PackedLibraryUtility.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/LVLibp/NI_PackedLibraryUtility.lvlib"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="Simple Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Simple Error Handler.vi"/>
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
				<Item Name="subElapsedTime.vi" Type="VI" URL="/&lt;vilib&gt;/express/express execution control/ElapsedTimeBlock.llb/subElapsedTime.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="Trim Whitespace One-Sided.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace One-Sided.vi"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
			</Item>
			<Item Name="labbCAN_Bus_API.lvlib" Type="Library" URL="../CETONI_SDK/lib/labview/labbCAN_Bus_API/labbCAN_Bus_API.lvlib"/>
			<Item Name="labbCAN_Pump_API.lvlib" Type="Library" URL="../CETONI_SDK/lib/labview/labbCAN_Pump_API/labbCAN_Pump_API.lvlib"/>
			<Item Name="labbCAN_Valve_API.lvlib" Type="Library" URL="../CETONI_SDK/lib/labview/labbCAN_Valve_API/labbCAN_Valve_API.lvlib"/>
			<Item Name="lvanlys.dll" Type="Document" URL="/&lt;resource&gt;/lvanlys.dll"/>
			<Item Name="dwf.dll" Type="Document" URL="/../Windows/System32/dwf.dll"/>
			<Item Name="TCxxxx.lvlib" Type="Library" URL="../Peltier controller TC/TCxxxx/TCxxxx.lvlib"/>
			<Item Name="Adresse.ctl" Type="VI" URL="../Peltier controller TC/TCxxxx/Controls/Adresse.ctl"/>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
