python -m nuitka \
          --follow-imports \
          --output-dir=build \
          --assume-yes-for-download \
          --macos-app-version=1.0 \
          --standalone \
          --onefile \
          --macos-create-app-bundle \
          --plugin-enable=pyqt5 \
          --macos-disable-console \
          --macos-app-icon=icon/plus.png \
          main_teacher.py
echo "add File_template"
cp -r File_template build/main_teacher.app/
echo "add database"
cp -r database build/main_teacher.app/
echo "add icon"
cp -r build/Resources build/main_teacher.app/Contents/
echo "add info.plist"
cp -r build/info.plist build/main_teacher.app/Contents/
echo "all done"
open build/