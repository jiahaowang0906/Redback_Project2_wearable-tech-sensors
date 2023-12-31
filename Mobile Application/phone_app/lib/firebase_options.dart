// File generated by FlutterFire CLI.
// ignore_for_file: lines_longer_than_80_chars, avoid_classes_with_only_static_members
import 'package:firebase_core/firebase_core.dart' show FirebaseOptions;
import 'package:flutter/foundation.dart'
    show defaultTargetPlatform, kIsWeb, TargetPlatform;

/// Default [FirebaseOptions] for use with your Firebase apps.
///
/// Example:
/// ```dart
/// import 'firebase_options.dart';
/// // ...
/// await Firebase.initializeApp(
///   options: DefaultFirebaseOptions.currentPlatform,
/// );
/// ```
class DefaultFirebaseOptions {
  static FirebaseOptions get currentPlatform {
    if (kIsWeb) {
      return web;
    }
    switch (defaultTargetPlatform) {
      case TargetPlatform.android:
        return android;
      case TargetPlatform.iOS:
        return ios;
      case TargetPlatform.macOS:
        return macos;
      case TargetPlatform.windows:
        throw UnsupportedError(
          'DefaultFirebaseOptions have not been configured for windows - '
          'you can reconfigure this by running the FlutterFire CLI again.',
        );
      case TargetPlatform.linux:
        throw UnsupportedError(
          'DefaultFirebaseOptions have not been configured for linux - '
          'you can reconfigure this by running the FlutterFire CLI again.',
        );
      default:
        throw UnsupportedError(
          'DefaultFirebaseOptions are not supported for this platform.',
        );
    }
  }

  static const FirebaseOptions web = FirebaseOptions(
    apiKey: 'AIzaSyBuCVsZ2tzU4BXkJbTeR9GyvuWwozhbwD0',
    appId: '1:721356738428:web:ff55cfe8ad848356c79ef9',
    messagingSenderId: '721356738428',
    projectId: 'fitnesstracker-9f782',
    authDomain: 'fitnesstracker-9f782.firebaseapp.com',
    storageBucket: 'fitnesstracker-9f782.appspot.com',
    measurementId: 'G-Q0W6SM84K5',
  );

  static const FirebaseOptions android = FirebaseOptions(
    apiKey: 'AIzaSyC_jSJIRcJtl8w7hsraE9HGLfkfC8v5ZZI',
    appId: '1:721356738428:android:8caf195d13c0c033c79ef9',
    messagingSenderId: '721356738428',
    projectId: 'fitnesstracker-9f782',
    storageBucket: 'fitnesstracker-9f782.appspot.com',
  );

  static const FirebaseOptions ios = FirebaseOptions(
    apiKey: 'AIzaSyCaiDMUgHUpU1O25ZzWuDKwkELBoYfIXio',
    appId: '1:721356738428:ios:0d4fd22ef06f94d4c79ef9',
    messagingSenderId: '721356738428',
    projectId: 'fitnesstracker-9f782',
    storageBucket: 'fitnesstracker-9f782.appspot.com',
    iosBundleId: 'com.example.phoneApp',
  );

  static const FirebaseOptions macos = FirebaseOptions(
    apiKey: 'AIzaSyCaiDMUgHUpU1O25ZzWuDKwkELBoYfIXio',
    appId: '1:721356738428:ios:c9d730ae88458a15c79ef9',
    messagingSenderId: '721356738428',
    projectId: 'fitnesstracker-9f782',
    storageBucket: 'fitnesstracker-9f782.appspot.com',
    iosBundleId: 'com.example.phoneApp.RunnerTests',
  );
}
