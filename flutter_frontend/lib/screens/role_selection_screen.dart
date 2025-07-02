import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../widgets/custom_button.dart';
import '../constants.dart';

class RoleSelectionScreen extends StatelessWidget {
  Future<void> _selectRole(BuildContext context, String role) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('role', role);
    Navigator.pushNamed(context, '/login');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Welcome !')),
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [lightGradientStart, lightGradientEnd],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
        ),
        padding: const EdgeInsets.all(24.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text(
              'Choisissez votre espace',
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              textAlign: TextAlign.center,
            ),
            SizedBox(height: 40),
            CustomButton(
              text: 'Je suis étudiant.e',
              color: primaryColor,
              onPressed: () => _selectRole(context, 'student'),
            ),
            SizedBox(height: 16),
            CustomButton(
              text: 'Je suis administrateur.trice',
              color: secondaryColor,
              onPressed: () => _selectRole(context, 'admin'),
            ),
            SizedBox(height: 16),
            CustomButton(
              text: 'Je suis Recruteur.trice',
              color: recruiterColor,
              onPressed: () => _selectRole(context, 'recruiter'),
            ),
          ],
        ),
      ),
    );
  }
}
