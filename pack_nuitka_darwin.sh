echo "which build do you want to pack?"
read -p "1. student 2. teacher 3. full: 4. test: " build_type

if [ $build_type == 1 ]
then
    echo "pack student"
    python3 -m nuitka \
          --follow-imports \
          --output-dir=build/student \
          --assume-yes-for-download \
          --macos-app-version=1.0 \
          --standalone \
          --onefile \
          --macos-create-app-bundle \
          --plugin-enable=pyqt5 \
          --macos-disable-console \
          --macos-app-icon=icon/icon.ico \
          student_entry.py
    echo "add File_template"
    cp -r File_template build/student/student_entry.app
    echo "add database"
    cp -r database build/student/student_entry.app
    echo "add signature"
    cp -r signature build/student/student_entry.app
    echo "add icon"
    cp -r build/student/Resources build/student/student_entry.app/Contents/
    echo "add info.plist"
    cp -r build/student/Info.plist build/student/student_entry.app/Contents/
    echo "all done"
    open build/
    exit 0

elif [ $build_type == 2 ]
then
    echo "pack teacher"
    python3 -m nuitka \
          --follow-imports \
          --output-dir=build/teacher \
          --assume-yes-for-download \
          --macos-app-version=1.0 \
          --standalone \
          --onefile \
          --macos-create-app-bundle \
          --plugin-enable=pyqt5 \
          --macos-disable-console \
          --macos-app-icon=icon/icon.ico \
          teacher_entry.py
    echo "add File_template"
    cp -r File_template build/teacher/teacher_entry.app
    echo "add database"
    cp -r database build/teacher/teacher_entry.app
    echo "add signature"
    cp -r signature build/teacher/teacher_entry.app
    echo "add icon"
    cp -r build/teacher/Resources build/teacher/teacher_entry.app/Contents/
    echo "add info.plist"
    cp -r build/teacher/Info.plist build/teacher/teacher_entry.app/Contents/
    echo "all done"
    open build/
    exit 0

elif [ $build_type == 3 ]
then
    echo "pack full"
    python3 -m nuitka \
          --follow-imports \
          --output-dir=build/full \
          --assume-yes-for-download \
          --macos-app-version=1.0 \
          --standalone \
          --onefile \
          --macos-create-app-bundle \
          --plugin-enable=pyqt5 \
          --macos-disable-console \
          --macos-app-icon=icon/icon.ico \
          full_entry.py
    echo "add File_template"
    cp -r File_template build/full/full_entry.app
    echo "add database"
    cp -r database build/full/full_entry.app
    echo "add signature"
    cp -r signature build/full/full_entry.app
    echo "add icon"
    cp -r build/full/Resources build/full/full_entry.app/Contents/
    echo "add info.plist"
    cp -r build/full/Info.plist build/full/full_entry.app/Contents/
    echo "all done"
    open build/
    exit 0

elif [ $build_type == 4 ]
then
    echo "pack test"
    python3 -m nuitka \
          --follow-imports \
          --output-dir=build/test \
          --assume-yes-for-download \
          --macos-app-version=1.0 \
          --standalone \
          --onefile \
          --macos-create-app-bundle \
          --plugin-enable=pyqt5 \
          --macos-disable-console \
          --macos-app-icon=icon/icon.ico \
          build_test.py
    echo "add icon"
    cp -r build/test/Resources build/test/build_test.app/Contents/
    echo "add info.plist"
    cp -r build/test/Info.plist build/test/build_test.app/Contents/
    echo "all done"
    open build/
    exit 0

else
    echo "wrong input"
    exit 1
fi