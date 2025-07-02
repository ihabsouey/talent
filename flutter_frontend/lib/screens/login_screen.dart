import 'package:flutter/material.dart';
import 'package:google_sign_in/google_sign_in.dart';
import '../widgets/custom_button.dart';
import '../widgets/rounded_text_field.dart';

class LoginScreen extends StatelessWidget {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();

  Future<void> _handleGoogleSignIn() async {
    final _googleSignIn = GoogleSignIn();
    try {
      await _googleSignIn.signIn();
    } catch (error) {
      // handle error
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Connexion')),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            CustomButton(
              text: 'Continue avec Google',
              color: Colors.redAccent,
              onPressed: _handleGoogleSignIn,
            ),
            SizedBox(height: 20),
            RoundedTextField(
              controller: emailController,
              hintText: 'Adresse mail',
            ),
            SizedBox(height: 10),
            RoundedTextField(
              controller: passwordController,
              hintText: 'Mot de passe',
              obscureText: true,
            ),
            SizedBox(height: 20),
            CustomButton(
              text: 'Connexion',
              onPressed: () {
                Navigator.pushReplacementNamed(context, '/home');
              },
            ),
            TextButton(
              onPressed: () {},
              child: Text('Mot de passe oublié ?'),
            ),
            Spacer(),
            TextButton(
              onPressed: () {},
              child: Text('Sign up'),
            )
          ],
        ),
      ),
    );
  }
}
