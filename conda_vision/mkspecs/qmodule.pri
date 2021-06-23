QMAKE_CFLAGS_WARN_ON += -Wno-expansion-to-defined
QMAKE_CXXFLAGS_WARN_ON += -Wno-expansion-to-defined
EXTRA_DEFINES += _X_INLINE=inline XK_dead_currency=0xfe6f _FORTIFY_SOURCE=2 XK_ISO_Level5_Lock=0xfe13 FC_WEIGHT_EXTRABLACK=215 FC_WEIGHT_ULTRABLACK=FC_WEIGHT_EXTRABLACK GLX_GLXEXT_PROTOTYPES
EXTRA_INCLUDEPATH += /home/conda/feedstock_root/build_artifacts/qt_1613665445340/work/openssl_hack/include /home/ruben/vision-course/conda_vision/include
EXTRA_LIBDIR += /home/ruben/vision-course/conda_vision/lib /home/ruben/vision-course/conda_vision/x86_64-conda-linux-gnu/sysroot/usr/lib64
!host_build|!cross_compile {
    QMAKE_LFLAGS+=-Wl,-rpath,/home/ruben/vision-course/conda_vision/lib -Wl,-rpath-link,/home/ruben/vision-course/conda_vision/lib -L/home/ruben/vision-course/conda_vision/lib
}
QT_CPU_FEATURES.x86_64 = mmx sse sse2
QT.global_private.enabled_features = sse2 alloca_h alloca dbus dbus-linked gui network posix_fallocate reduce_exports reduce_relocations sql system-zlib testlib widgets xml
QT.global_private.disabled_features = alloca_malloc_h android-style-assets avx2 private_tests gc_binaries libudev release_tools stack-protector-strong
PKG_CONFIG_EXECUTABLE = /home/ruben/vision-course/conda_vision/bin/pkg-config
QMAKE_LIBS_DBUS = /home/ruben/vision-course/conda_vision/lib/libdbus-1.so
QMAKE_INCDIR_DBUS = /home/ruben/vision-course/conda_vision/include/dbus-1.0 /home/ruben/vision-course/conda_vision/lib/dbus-1.0/include
QT_COORD_TYPE = double
QMAKE_LIBS_ZLIB = /home/ruben/vision-course/conda_vision/lib/libz.so
CONFIG += use_gold_linker sse2 aesni compile_examples enable_new_dtags largefile optimize_size precompile_header rdrnd shani sse3 ssse3 sse4_1 sse4_2 x86SimdAlways
QT_BUILD_PARTS += libs tools
QT_HOST_CFLAGS_DBUS += -I/home/ruben/vision-course/conda_vision/include/dbus-1.0 -I/home/ruben/vision-course/conda_vision/lib/dbus-1.0/include
