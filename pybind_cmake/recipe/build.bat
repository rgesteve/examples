set "CMAKE_CONFIG=Release"
if errorlevel 1 exit 1

set "VCPKG_ROOT=c:\users\perf\documents\projects\vcpkg"
if errorlevel 1 exit 1

mkdir build_%CMAKE_CONFIG%
if errorlevel 1 exit 1

pushd build_%CMAKE_CONFIG%
if errorlevel 1 exit 1

cmake -G "Visual Studio 15 2017 Win64" ^
      -DCMAKE_TOOLCHAIN_FILE=%VCPKG_ROOT%\scripts\buildsystems\vcpkg.cmake
      -DCMAKE_BUILD_TYPE:STRING=%CMAKE_CONFIG% ^
      -DCMAKE_INSTALL_PREFIX:PATH="%LIBRARY_PREFIX%" ^
      "%SRC_DIR%"
if errorlevel 1 exit 1

cmake --build . --target install --config %CMAKE_CONFIG%
if errorlevel 1 exit 1

popd
if errorlevel 1 exit 1
