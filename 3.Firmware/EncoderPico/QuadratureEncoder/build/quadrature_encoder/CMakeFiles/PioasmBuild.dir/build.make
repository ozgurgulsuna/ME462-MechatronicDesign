# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.23

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build

# Utility rule file for PioasmBuild.

# Include any custom commands dependencies for this target.
include quadrature_encoder/CMakeFiles/PioasmBuild.dir/compiler_depend.make

# Include the progress variables for this target.
include quadrature_encoder/CMakeFiles/PioasmBuild.dir/progress.make

quadrature_encoder/CMakeFiles/PioasmBuild: quadrature_encoder/CMakeFiles/PioasmBuild-complete

quadrature_encoder/CMakeFiles/PioasmBuild-complete: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-install
quadrature_encoder/CMakeFiles/PioasmBuild-complete: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-mkdir
quadrature_encoder/CMakeFiles/PioasmBuild-complete: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-download
quadrature_encoder/CMakeFiles/PioasmBuild-complete: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-update
quadrature_encoder/CMakeFiles/PioasmBuild-complete: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-patch
quadrature_encoder/CMakeFiles/PioasmBuild-complete: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-configure
quadrature_encoder/CMakeFiles/PioasmBuild-complete: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-build
quadrature_encoder/CMakeFiles/PioasmBuild-complete: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-install
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Completed 'PioasmBuild'"
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder && /usr/bin/cmake -E make_directory /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder/CMakeFiles
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder && /usr/bin/cmake -E touch /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder/CMakeFiles/PioasmBuild-complete
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder && /usr/bin/cmake -E touch /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-done

quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-build: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-configure
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Performing build step for 'PioasmBuild'"
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/pioasm && $(MAKE)

quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-configure: quadrature_encoder/pioasm/tmp/PioasmBuild-cfgcmd.txt
quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-configure: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-patch
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Performing configure step for 'PioasmBuild'"
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/pioasm && /usr/bin/cmake "-GUnix Makefiles" /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/Dependencies/pico-sdk/tools/pioasm
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/pioasm && /usr/bin/cmake -E touch /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-configure

quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-download: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-source_dirinfo.txt
quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-download: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-mkdir
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "No download step for 'PioasmBuild'"
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder && /usr/bin/cmake -E echo_append
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder && /usr/bin/cmake -E touch /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-download

quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-install: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-build
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "No install step for 'PioasmBuild'"
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/pioasm && /usr/bin/cmake -E echo_append
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/pioasm && /usr/bin/cmake -E touch /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-install

quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-mkdir:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Creating directories for 'PioasmBuild'"
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder && /usr/bin/cmake -P /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder/pioasm/tmp/PioasmBuild-mkdirs.cmake
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder && /usr/bin/cmake -E touch /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-mkdir

quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-patch: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-update
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "No patch step for 'PioasmBuild'"
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder && /usr/bin/cmake -E echo_append
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder && /usr/bin/cmake -E touch /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-patch

quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-update: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-download
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "No update step for 'PioasmBuild'"
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder && /usr/bin/cmake -E echo_append
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder && /usr/bin/cmake -E touch /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-update

PioasmBuild: quadrature_encoder/CMakeFiles/PioasmBuild
PioasmBuild: quadrature_encoder/CMakeFiles/PioasmBuild-complete
PioasmBuild: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-build
PioasmBuild: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-configure
PioasmBuild: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-download
PioasmBuild: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-install
PioasmBuild: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-mkdir
PioasmBuild: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-patch
PioasmBuild: quadrature_encoder/pioasm/src/PioasmBuild-stamp/PioasmBuild-update
PioasmBuild: quadrature_encoder/CMakeFiles/PioasmBuild.dir/build.make
.PHONY : PioasmBuild

# Rule to build all files generated by this target.
quadrature_encoder/CMakeFiles/PioasmBuild.dir/build: PioasmBuild
.PHONY : quadrature_encoder/CMakeFiles/PioasmBuild.dir/build

quadrature_encoder/CMakeFiles/PioasmBuild.dir/clean:
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder && $(CMAKE_COMMAND) -P CMakeFiles/PioasmBuild.dir/cmake_clean.cmake
.PHONY : quadrature_encoder/CMakeFiles/PioasmBuild.dir/clean

quadrature_encoder/CMakeFiles/PioasmBuild.dir/depend:
	cd /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/quadrature_encoder /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder /mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder/CMakeFiles/PioasmBuild.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : quadrature_encoder/CMakeFiles/PioasmBuild.dir/depend
