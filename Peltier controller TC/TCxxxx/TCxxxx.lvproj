<?xml version='1.0' encoding='UTF-8'?>
<Project Name="Template - Generic.lvproj" Type="Project" LVVersion="12008004" URL="/&lt;instrlib&gt;/_Template - Generic/Template - Generic.lvproj">
	<Property Name="Instrument Driver" Type="Str">True</Property>
	<Property Name="NI.Project.Description" Type="Str">This project is used by developers to edit API and example files for LabVIEW Plug and Play instrument drivers.</Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="CCSymbols" Type="Str">OS,Win;CPU,x86;</Property>
		<Property Name="NI.SortType" Type="Int">3</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Examples" Type="Folder">
			<Item Name="Advanced Serial Write and Read.vi" Type="VI" URL="/&lt;instrlib&gt;/TCxxxx/Examples/Advanced Serial Write and Read.vi"/>
			<Item Name="FirstSteps.vi" Type="VI" URL="/&lt;instrlib&gt;/TCxxxx/Examples/FirstSteps.vi"/>
			<Item Name="FirstStepsRead.vi" Type="VI" URL="/&lt;instrlib&gt;/TCxxxx/Examples/FirstStepsRead.vi"/>
		</Item>
		<Item Name="Controls" Type="Folder">
			<Item Name="Adresse.ctl" Type="VI" URL="/&lt;instrlib&gt;/TCxxxx/Controls/Adresse.ctl"/>
		</Item>
		<Item Name="Documentation" Type="Folder">
			<Item Name="TCxxxx.pdf" Type="Document" URL="/&lt;instrlib&gt;/TCxxxx/Documentation/TCxxxx.pdf"/>
			<Item Name="TCxxxx_lvlib_ReadWord.rtf" Type="Document" URL="/&lt;instrlib&gt;/TCxxxx/Documentation/TCxxxx_lvlib_ReadWord.rtf"/>
		</Item>
		<Item Name="TCxxxx.lvlib" Type="Library" URL="/&lt;instrlib&gt;/TCxxxx/TCxxxx.lvlib"/>
		<Item Name="TCxxxx.aliases" Type="Document" URL="/&lt;instrlib&gt;/TCxxxx/TCxxxx.aliases"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="General Error Handler CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler CORE.vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="Simple Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Simple Error Handler.vi"/>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="CoolTronic TCxxxx Installer" Type="Installer">
				<Property Name="Destination[0].name" Type="Str">TCxxxx</Property>
				<Property Name="Destination[0].parent" Type="Str">{DF5B8568-3919-47DB-B51E-F4E8682F1AEA}</Property>
				<Property Name="Destination[0].tag" Type="Str">{77F68989-8325-45BF-B340-57B71C94F59A}</Property>
				<Property Name="Destination[0].type" Type="Str">userFolder</Property>
				<Property Name="Destination[1].name" Type="Str">Controls</Property>
				<Property Name="Destination[1].parent" Type="Str">{77F68989-8325-45BF-B340-57B71C94F59A}</Property>
				<Property Name="Destination[1].tag" Type="Str">{0C4650E1-08E0-4088-AEBA-FECD44DF15EC}</Property>
				<Property Name="Destination[1].type" Type="Str">userFolder</Property>
				<Property Name="Destination[2].name" Type="Str">Documentation</Property>
				<Property Name="Destination[2].parent" Type="Str">{77F68989-8325-45BF-B340-57B71C94F59A}</Property>
				<Property Name="Destination[2].tag" Type="Str">{0E0E173D-281F-4828-B2A2-A6CC3989504D}</Property>
				<Property Name="Destination[2].type" Type="Str">userFolder</Property>
				<Property Name="Destination[3].name" Type="Str">Examples</Property>
				<Property Name="Destination[3].parent" Type="Str">{77F68989-8325-45BF-B340-57B71C94F59A}</Property>
				<Property Name="Destination[3].tag" Type="Str">{7D18411E-7B10-4E29-93B1-A7A098ECEB65}</Property>
				<Property Name="Destination[3].type" Type="Str">userFolder</Property>
				<Property Name="Destination[4].name" Type="Str">Public</Property>
				<Property Name="Destination[4].parent" Type="Str">{77F68989-8325-45BF-B340-57B71C94F59A}</Property>
				<Property Name="Destination[4].tag" Type="Str">{5E88FA34-BA42-4345-95E8-F5FEA052CE44}</Property>
				<Property Name="Destination[4].type" Type="Str">userFolder</Property>
				<Property Name="Destination[5].name" Type="Str">Data</Property>
				<Property Name="Destination[5].parent" Type="Str">{5E88FA34-BA42-4345-95E8-F5FEA052CE44}</Property>
				<Property Name="Destination[5].tag" Type="Str">{A1052DD4-FD61-4D6D-9F6C-184B88E3833D}</Property>
				<Property Name="Destination[5].type" Type="Str">userFolder</Property>
				<Property Name="Destination[6].name" Type="Str">Utility</Property>
				<Property Name="Destination[6].parent" Type="Str">{5E88FA34-BA42-4345-95E8-F5FEA052CE44}</Property>
				<Property Name="Destination[6].tag" Type="Str">{2B1FF5D4-D00E-45C2-9BA8-460EE6984B10}</Property>
				<Property Name="Destination[6].type" Type="Str">userFolder</Property>
				<Property Name="DestinationCount" Type="Int">7</Property>
				<Property Name="DistPart[0].flavorID" Type="Str">DefaultFull</Property>
				<Property Name="DistPart[0].productID" Type="Str">{3854EDA2-20A9-4A25-9A29-47A8BBF48DEB}</Property>
				<Property Name="DistPart[0].productName" Type="Str">NI LabVIEW Run-Time Engine 2012</Property>
				<Property Name="DistPart[0].upgradeCode" Type="Str">{20385C41-50B1-4416-AC2A-F7D6423A9BD6}</Property>
				<Property Name="DistPartCount" Type="Int">1</Property>
				<Property Name="INST_author" Type="Str">tameq</Property>
				<Property Name="INST_buildLocation" Type="Path">../builds/TCxxxx/CoolTronic TCxxxx Installer</Property>
				<Property Name="INST_buildLocation.type" Type="Str">relativeToCommon</Property>
				<Property Name="INST_buildSpecName" Type="Str">CoolTronic TCxxxx Installer</Property>
				<Property Name="INST_defaultDir" Type="Str">{DF5B8568-3919-47DB-B51E-F4E8682F1AEA}</Property>
				<Property Name="INST_productName" Type="Str">TCxxxx</Property>
				<Property Name="INST_productVersion" Type="Str">1.0.0</Property>
				<Property Name="InstSpecBitness" Type="Str">32-bit</Property>
				<Property Name="InstSpecVersion" Type="Str">12008024</Property>
				<Property Name="MSI_arpCompany" Type="Str">CoolTronic</Property>
				<Property Name="MSI_distID" Type="Str">{9741A6F0-9BD0-4EBA-BC86-00BF778ABD0B}</Property>
				<Property Name="MSI_osCheck" Type="Int">0</Property>
				<Property Name="MSI_upgradeCode" Type="Str">{AFB82950-3335-4094-BCA9-ED2A6D1BF67C}</Property>
				<Property Name="RegDest[0].dirName" Type="Str">Software</Property>
				<Property Name="RegDest[0].dirTag" Type="Str">{DDFAFC8B-E728-4AC8-96DE-B920EBB97A86}</Property>
				<Property Name="RegDest[0].parentTag" Type="Str">2</Property>
				<Property Name="RegDestCount" Type="Int">1</Property>
				<Property Name="Source[0].dest" Type="Str">{77F68989-8325-45BF-B340-57B71C94F59A}</Property>
				<Property Name="Source[0].name" Type="Str">TCxxxx.lvlib</Property>
				<Property Name="Source[0].tag" Type="Ref">/My Computer/TCxxxx.lvlib</Property>
				<Property Name="Source[0].type" Type="Str">File</Property>
				<Property Name="Source[1].dest" Type="Str">{0C4650E1-08E0-4088-AEBA-FECD44DF15EC}</Property>
				<Property Name="Source[1].name" Type="Str">Adresse.ctl</Property>
				<Property Name="Source[1].tag" Type="Ref">/My Computer/Controls/Adresse.ctl</Property>
				<Property Name="Source[1].type" Type="Str">File</Property>
				<Property Name="Source[10].dest" Type="Str">{A1052DD4-FD61-4D6D-9F6C-184B88E3833D}</Property>
				<Property Name="Source[10].name" Type="Str">ReadInt.vi</Property>
				<Property Name="Source[10].tag" Type="Ref">/My Computer/TCxxxx.lvlib/Public/Data/ReadInt.vi</Property>
				<Property Name="Source[10].type" Type="Str">File</Property>
				<Property Name="Source[11].dest" Type="Str">{A1052DD4-FD61-4D6D-9F6C-184B88E3833D}</Property>
				<Property Name="Source[11].name" Type="Str">ReadWord.vi</Property>
				<Property Name="Source[11].tag" Type="Ref">/My Computer/TCxxxx.lvlib/Public/Data/ReadWord.vi</Property>
				<Property Name="Source[11].type" Type="Str">File</Property>
				<Property Name="Source[12].dest" Type="Str">{A1052DD4-FD61-4D6D-9F6C-184B88E3833D}</Property>
				<Property Name="Source[12].name" Type="Str">Update.vi</Property>
				<Property Name="Source[12].tag" Type="Ref">/My Computer/TCxxxx.lvlib/Public/Data/Update.vi</Property>
				<Property Name="Source[12].type" Type="Str">File</Property>
				<Property Name="Source[13].dest" Type="Str">{A1052DD4-FD61-4D6D-9F6C-184B88E3833D}</Property>
				<Property Name="Source[13].name" Type="Str">WriteInt.vi</Property>
				<Property Name="Source[13].tag" Type="Ref">/My Computer/TCxxxx.lvlib/Public/Data/WriteInt.vi</Property>
				<Property Name="Source[13].type" Type="Str">File</Property>
				<Property Name="Source[14].dest" Type="Str">{A1052DD4-FD61-4D6D-9F6C-184B88E3833D}</Property>
				<Property Name="Source[14].name" Type="Str">WriteWord.vi</Property>
				<Property Name="Source[14].tag" Type="Ref">/My Computer/TCxxxx.lvlib/Public/Data/WriteWord.vi</Property>
				<Property Name="Source[14].type" Type="Str">File</Property>
				<Property Name="Source[15].dest" Type="Str">{2B1FF5D4-D00E-45C2-9BA8-460EE6984B10}</Property>
				<Property Name="Source[15].name" Type="Str">Error Query.vi</Property>
				<Property Name="Source[15].tag" Type="Ref">/My Computer/TCxxxx.lvlib/Public/Utility/Error Query.vi</Property>
				<Property Name="Source[15].type" Type="Str">File</Property>
				<Property Name="Source[16].dest" Type="Str">{2B1FF5D4-D00E-45C2-9BA8-460EE6984B10}</Property>
				<Property Name="Source[16].name" Type="Str">GetStatus.vi</Property>
				<Property Name="Source[16].tag" Type="Ref">/My Computer/TCxxxx.lvlib/Public/Utility/GetStatus.vi</Property>
				<Property Name="Source[16].type" Type="Str">File</Property>
				<Property Name="Source[17].dest" Type="Str">{2B1FF5D4-D00E-45C2-9BA8-460EE6984B10}</Property>
				<Property Name="Source[17].name" Type="Str">Read.vi</Property>
				<Property Name="Source[17].tag" Type="Ref">/My Computer/TCxxxx.lvlib/Public/Utility/Read.vi</Property>
				<Property Name="Source[17].type" Type="Str">File</Property>
				<Property Name="Source[18].dest" Type="Str">{2B1FF5D4-D00E-45C2-9BA8-460EE6984B10}</Property>
				<Property Name="Source[18].name" Type="Str">Write.vi</Property>
				<Property Name="Source[18].tag" Type="Ref">/My Computer/TCxxxx.lvlib/Public/Utility/Write.vi</Property>
				<Property Name="Source[18].type" Type="Str">File</Property>
				<Property Name="Source[19].dest" Type="Str">{77F68989-8325-45BF-B340-57B71C94F59A}</Property>
				<Property Name="Source[19].name" Type="Str">TCxxxx.aliases</Property>
				<Property Name="Source[19].tag" Type="Ref">/My Computer/TCxxxx.aliases</Property>
				<Property Name="Source[19].type" Type="Str">File</Property>
				<Property Name="Source[2].dest" Type="Str">{0E0E173D-281F-4828-B2A2-A6CC3989504D}</Property>
				<Property Name="Source[2].name" Type="Str">TCxxxx Readme.html</Property>
				<Property Name="Source[2].tag" Type="Ref"></Property>
				<Property Name="Source[2].type" Type="Str">File</Property>
				<Property Name="Source[3].dest" Type="Str">{0E0E173D-281F-4828-B2A2-A6CC3989504D}</Property>
				<Property Name="Source[3].name" Type="Str">TCxxxx.pdf</Property>
				<Property Name="Source[3].tag" Type="Ref"></Property>
				<Property Name="Source[3].type" Type="Str">File</Property>
				<Property Name="Source[4].dest" Type="Str">{7D18411E-7B10-4E29-93B1-A7A098ECEB65}</Property>
				<Property Name="Source[4].name" Type="Str">Advanced Serial Write and Read.vi</Property>
				<Property Name="Source[4].tag" Type="Ref">/My Computer/Examples/Advanced Serial Write and Read.vi</Property>
				<Property Name="Source[4].type" Type="Str">File</Property>
				<Property Name="Source[5].dest" Type="Str">{7D18411E-7B10-4E29-93B1-A7A098ECEB65}</Property>
				<Property Name="Source[5].name" Type="Str">FirstSteps.vi</Property>
				<Property Name="Source[5].tag" Type="Ref">/My Computer/Examples/FirstSteps.vi</Property>
				<Property Name="Source[5].type" Type="Str">File</Property>
				<Property Name="Source[6].dest" Type="Str">{7D18411E-7B10-4E29-93B1-A7A098ECEB65}</Property>
				<Property Name="Source[6].name" Type="Str">FirstStepsRead.vi</Property>
				<Property Name="Source[6].tag" Type="Ref">/My Computer/Examples/FirstStepsRead.vi</Property>
				<Property Name="Source[6].type" Type="Str">File</Property>
				<Property Name="Source[7].dest" Type="Str">{5E88FA34-BA42-4345-95E8-F5FEA052CE44}</Property>
				<Property Name="Source[7].name" Type="Str">Close.vi</Property>
				<Property Name="Source[7].tag" Type="Ref">/My Computer/TCxxxx.lvlib/Public/Close.vi</Property>
				<Property Name="Source[7].type" Type="Str">File</Property>
				<Property Name="Source[8].dest" Type="Str">{5E88FA34-BA42-4345-95E8-F5FEA052CE44}</Property>
				<Property Name="Source[8].name" Type="Str">Initialize.vi</Property>
				<Property Name="Source[8].tag" Type="Ref">/My Computer/TCxxxx.lvlib/Public/Initialize.vi</Property>
				<Property Name="Source[8].type" Type="Str">File</Property>
				<Property Name="Source[9].dest" Type="Str">{5E88FA34-BA42-4345-95E8-F5FEA052CE44}</Property>
				<Property Name="Source[9].name" Type="Str">VI Tree.vi</Property>
				<Property Name="Source[9].tag" Type="Ref">/My Computer/TCxxxx.lvlib/Public/VI Tree.vi</Property>
				<Property Name="Source[9].type" Type="Str">File</Property>
				<Property Name="SourceCount" Type="Int">20</Property>
			</Item>
		</Item>
	</Item>
</Project>
