add_executable(pio_quadrature_encoder_multi)

pico_generate_pio_header(pio_quadrature_encoder_multi ${CMAKE_CURRENT_LIST_DIR}/quadrature_encoder.pio)

target_sources(pio_quadrature_encoder_multi PRIVATE quadrature_encoder.c)

target_link_libraries(pio_quadrature_encoder_multi PRIVATE
        pico_stdlib
        pico_multicore
        hardware_pio
        )

pico_enable_stdio_usb(pio_quadrature_encoder_multi 1)

pico_add_extra_outputs(pio_quadrature_encoder_multi)

# add url via pico_set_program_url
example_auto_set_url(pio_quadrature_encoder_multi)
