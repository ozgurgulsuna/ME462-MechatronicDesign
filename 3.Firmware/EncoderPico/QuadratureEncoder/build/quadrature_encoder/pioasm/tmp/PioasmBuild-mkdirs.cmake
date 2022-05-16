# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/Dependencies/pico-sdk/tools/pioasm"
  "/mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/pioasm"
  "/mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder/pioasm"
  "/mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder/pioasm/tmp"
  "/mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder/pioasm/src/PioasmBuild-stamp"
  "/mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder/pioasm/src"
  "/mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder/pioasm/src/PioasmBuild-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/mnt/F86A888E6A884AF8/2021-22/Okul/Dersler/ME462/3.Firmware/EncoderPico/QuadratureEncoder/build/quadrature_encoder/pioasm/src/PioasmBuild-stamp/${subDir}")
endforeach()
