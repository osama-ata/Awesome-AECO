# Awesome AECO [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

AECO stands for Architecture, Engineering, Construction, and Operations. It refers to the integrated process of designing, building, and managing a building or infrastructure project throughout its lifecycle, from the initial design to ongoing maintenance and operations. This process involves various disciplines working together to create and manage a built environment.

> A curated list of awesome AECO resources, tools, and technologies.
> Inspired by [Awesome](https://github.com/sindresorhus/awesome).

## Contents

- [Awesome AECO](#awesome-aeco-)
  - [Contents](#contents)
  - [BIM (Building Information Modeling)](#bim-building-information-modeling)
  - [CAD (Computer-Aided Design)](#cad-computer-aided-design)
  - [Revit Plugins \& Extensions](#revit-plugins--extensions)
  - [Simulation \& Analysis](#simulation--analysis)
  - [Parametric \& Computational Design](#parametric--computational-design)
  - [IoT \& Smart Buildings](#iot--smart-buildings)
  - [Facility \& Asset Management](#facility--asset-management)
  - [Generative Design](#generative-design)
  - [Construction Automation \& Robotics](#construction-automation--robotics)
  - [Digital Twins](#digital-twins)
  - [GIS \& Mapping](#gis--mapping)
  - [Project Management](#project-management)
  - [Contribute](#contribute)

---

## BIM (Building Information Modeling)

- **IfcOpenShell**
  Open-source toolkit and geometry engine for BuildingSMART IFC files. Enables reading, writing, and modifying BIM models via a C++ library and Python API.
  *GitHub: [IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell)*

- **xBIM Toolkit**
  The eXtensible BIM Toolkit for .NET, providing libraries to work with IFC data (read, create, validate). Allows developers on the Microsoft stack to build BIM applications.
  *GitHub: [xBimTeam/XbimEssentials](https://github.com/xBimTeam/XbimEssentials)*

- **BIMserver**
  Open-source BIM server platform (Java) that stores and manages building models using IFC. Acts as a model database with versioning and multi-user collaboration.
  *GitHub: [opensourceBIM/BIMserver](https://github.com/opensourceBIM/BIMserver)*

- **IFC.js**
  JavaScript toolkit (WASM-powered) for bringing IFC BIM data into web applications. Includes `web-ifc` for fast parsing and `web-ifc-three` for viewing in Three.js.
  *GitHub: [ThatOpen/engine_web-ifc](https://github.com/ThatOpen/engine_web-ifc)*

- **Speckle**
  Open-source AEC data platform ("Git for BIM") that enables real-time collaboration and interoperability by streaming geometry and data between design tools.
  *GitHub: [specklesystems/speckle-server](https://github.com/specklesystems/speckle-server)*

- **BHoM (Buildings and Habitats object Model)**
  A collaborative computational framework and data schema for the built environment. Defines a core object model for AEC domains (structure, environment, MEP, etc.).
  *GitHub: [BHoM/BHoM](https://github.com/BHoM/BHoM)*

- **Revit API Samples**
  Official Autodesk repositories demonstrating Revit API usage for automation and plugin development.
  *GitHub: [Autodesk/revit-api](https://github.com/Autodesk/revit-api)*

- **BIMsurfer**
  Web-based BIM viewer for IFC models with clash detection and collaboration features.
  *GitHub: [opensourceBIM/BIMsurfer](https://github.com/opensourceBIM/BIMsurfer)*

## CAD (Computer-Aided Design)

- **FreeCAD**
  Free, open-source parametric 3D CAD modeler with a modular architecture. Includes an Arch Workbench for BIM and supports exporting to IFC, DWG, and STEP.
  *GitHub: [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD)*

- **LibreCAD**
  Open-source 2D CAD drawing tool based on QCAD's community edition. Provides a cross-platform GUI for drafting with DXF/DWG support.
  *GitHub: [LibreCAD/LibreCAD](https://github.com/LibreCAD/LibreCAD)*

- **BRL-CAD**
  Mature open-source solid modeling system featuring a powerful CSG geometry engine and high-performance ray tracing.
  *GitHub: [BRL-CAD/brlcad](https://github.com/BRL-CAD/brlcad)*

- **OpenSCAD**
  "The Programmer's Solid 3D CAD Modeller." Users create 3D models by writing scripts that define primitives and boolean operations.
  *GitHub: [openscad/openscad](https://github.com/openscad/openscad)*

- **SolveSpace**
  A lightweight, parametric 2D/3D CAD program supporting constraint-based sketching and exports to STEP/DXF/STL.
  *GitHub: [solvespace/solvespace](https://github.com/solvespace/solvespace)*

- **CadQuery**
  Python-based parametric CAD scripting framework for mechanical and architectural design.
  *GitHub: [CadQuery/cadquery](https://github.com/CadQuery/cadquery)*

## Revit Plugins & Extensions

- **pyRevit**
  A rapid-development environment for Autodesk Revit. Lets users create custom tools in IronPython or CPython with an extensive API.
  *GitHub: [pyrevitlabs/pyRevit](https://github.com/pyrevitlabs/pyRevit)*

- **RevitLookup**
  Interactive BIM database explorer for Revit. Inspects data of selected elements (parameters, properties) in real-time.
  *GitHub: [jeremytammik/RevitLookup](https://github.com/jeremytammik/RevitLookup)*

- **Rhino.Inside Revit**
  Embeds McNeel Rhino 3D and Grasshopper into Revit's environment, enabling seamless transfer of geometry and parameters.
  *GitHub: [mcneel/rhino.inside-revit](https://github.com/mcneel/rhino.inside-revit)*

- **IFC Exporter for Revit**
  The open-source IFC plugin used by Revit for improved IFC support (IFC2x3/IFC4).
  *GitHub: [Autodesk/revit-ifc](https://github.com/Autodesk/revit-ifc)*

## Simulation & Analysis

- **EnergyPlus**
  The DOE's flagship whole-building energy simulation engine. Models heating/cooling loads, HVAC systems, and energy consumption.
  *GitHub: [NREL/EnergyPlus](https://github.com/NREL/EnergyPlus)*

- **OpenStudio**
  A cross-platform collection of tools for whole-building energy modeling that sits on top of EnergyPlus.
  *GitHub: [NREL/OpenStudio](https://github.com/NREL/OpenStudio)*

- **Ladybug Tools**
  Suite of open-source environmental analysis tools connecting CAD modeling to physics engines (e.g., Ladybug for solar analysis, Honeybee for energy/daylight).
  *GitHub: [ladybug-tools/ladybug](https://github.com/ladybug-tools/ladybug)*

- **Radiance**
  Industry-standard lighting simulation suite for evaluating daylight and electric lighting, producing accurate luminance values.
  *GitHub: [LBNL-ETA/Radiance](https://github.com/LBNL-ETA/Radiance)*

- **OpenFOAM**
  Computational fluid dynamics (CFD) toolkit for airflow and thermal simulations.
  *GitHub: [OpenFOAM/OpenFOAM-dev](https://github.com/OpenFOAM/OpenFOAM-dev)*

- **OpenSees**
  Open System for Earthquake Engineering Simulation. Framework for structural FEA and seismic simulation of structures.
  *GitHub: [OpenSees/OpenSees](https://github.com/OpenSees/OpenSees)*

## Parametric & Computational Design

- **Dynamo**
  Open-source visual programming platform for design automation. Popular for generative design and automating repetitive tasks in BIM.
  *GitHub: [DynamoDS/Dynamo](https://github.com/DynamoDS/Dynamo)*

- **COMPAS**
  Python-based computational framework for architecture, engineering, and digital fabrication.
  *GitHub: [compas-dev/compas](https://github.com/compas-dev/compas)*

- **Rhino.Compute**
  REST geometry server based on the Rhino 3D geometry kernel. Allows programmatic, headless access to Rhino's modeling capabilities.
  *GitHub: [mcneel/compute.rhino3d](https://github.com/mcneel/compute.rhino3d)*

- **BlenderBIM**
  Blender add-on for BIM workflows, supporting IFC import/export and parametric modeling.
  *GitHub: [blenderbim/blenderbim](https://github.com/blenderbim/blenderbim)*

- **Grasshopper-IFC**
  Grasshopper plugin for generating IFC-compliant geometries in Rhino.
  *GitHub: [MadsHolten/IFC-Grasshopper](https://github.com/MadsHolten/IFC-Grasshopper)*

## IoT & Smart Buildings

- **Home Assistant**
  Platform for smart home automation and IoT device integration with a focus on local control and privacy.
  *GitHub: [home-assistant/core](https://github.com/home-assistant/core)*

- **openHAB**
  Vendor-agnostic open-source software for integrating and controlling smart building devices.
  *GitHub: [openhab/openhab-addons](https://github.com/openhab/openhab-addons)*

- **Eclipse VOLTTRON**
  Platform for distributed sensing and control of building systems. Provides services to collect real-time data from building equipment.
  *GitHub: [VOLTTRON/volttron](https://github.com/VOLTTRON/volttron)*

- **EdgeX Foundry**
  Modular IoT platform for managing sensors and data in smart buildings.
  *GitHub: [edgexfoundry/edgex-go](https://github.com/edgexfoundry/edgex-go)*

- **ThingsBoard**
  Open-source IoT platform for device management, data visualization, and analytics.
  *GitHub: [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard)*

## Facility & Asset Management

- **Condo**
  Open-source property management SaaS for tracking maintenance tickets, resident contacts, and fee payments.
  *GitHub: [open-condo-software/condo](https://github.com/open-condo-software/condo)*

- **Atlas CMMS**
  Self-hosted Computerized Maintenance Management System. Allows teams to schedule work orders and manage inventory.
  *GitHub: [Grashjs/cmms](https://github.com/Grashjs/cmms)*

## Generative Design

- **Anton**
  Generative design framework for Blender leveraging topology optimization as a form-finding method.
  *GitHub: [senthurayyappan/anton](https://github.com/senthurayyappan/anton)*

- **Design Explorer**
  Web application for exploring multi-dimensional design spaces, used to visualize options from parametric studies.
  *GitHub: [tt-acm/DesignExplorer](https://github.com/tt-acm/DesignExplorer)*

## Construction Automation & Robotics

- **ROS (Robot Operating System)**
  Leading middleware for robotics, used in AEC to prototype construction robots or automation equipment.
  *GitHub: [ros/ros](https://github.com/ros/ros)*

- **Gazebo Simulator**
  High-fidelity 3D robotics simulator used to test construction robotics or automated equipment virtually.
  *GitHub: [gazebosim/gz-sim](https://github.com/gazebosim/gz-sim)*

## Digital Twins

- **iTwin.js**
  Open-source library from Bentley for creating and visualizing infrastructure digital twins.
  *GitHub: [iTwin/itwinjs-core](https://github.com/iTwin/itwinjs-core)*

- **Digital Twin Toolkit**
  Framework for creating digital twins of buildings and infrastructure.
  *GitHub: [digitaltwinconsortium/DigitalTwinToolkit](https://github.com/digitaltwinconsortium/DigitalTwinToolkit)*

## GIS & Mapping

- **QGIS**
  Free, open-source GIS for viewing, editing, and analyzing geospatial data.
  *GitHub: [qgis/QGIS](https://github.com/qgis/QGIS)*

- **CesiumJS**
  JavaScript library for 3D globes and map visualization, capable of streaming BIM data in a geospatial context.
  *GitHub: [CesiumGS/cesium](https://github.com/CesiumGS/cesium)*

- **OpenLayers**
  High-performance JS library for interactive maps on the web.
  *GitHub: [openlayers/openlayers](https://github.com/openlayers/openlayers)*

## Project Management

- **OpenProject**
  Collaborative project management tool with Gantt charts, Agile workflows, and BIM integration.
  *GitHub: [opf/openproject](https://github.com/opf/openproject)*

- **LibrePlan**
  Resource planning and scheduling software for construction projects.
  *GitHub: [LibrePlan/libreplan](https://github.com/LibrePlan/libreplan)*

## Contribute

Contributions welcome! Read the [contribution guidelines](contributing.md) first.
