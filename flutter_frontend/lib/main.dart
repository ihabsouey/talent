import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'constants.dart';
import 'screens/onboarding_screen.dart';
import 'screens/role_selection_screen.dart';
import 'screens/login_screen.dart';
import 'screens/home_screen.dart';
import 'screens/offer_detail_screen.dart';

void main() {
  runApp(TalentApp());
}

class TalentApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Talent',
      theme: ThemeData(
        primaryColor: primaryColor,
        colorScheme: ColorScheme.fromSwatch().copyWith(
          primary: primaryColor,
          secondary: secondaryColor,
        ),
        textTheme: GoogleFonts.poppinsTextTheme(),
      ),
      initialRoute: '/',
      routes: {
        '/': (context) => OnboardingScreen(),
        '/role': (context) => RoleSelectionScreen(),
        '/login': (context) => LoginScreen(),
        '/home': (context) => HomeScreen(),
        '/detail': (context) => OfferDetailScreen(),
      },
    );
  }
}
