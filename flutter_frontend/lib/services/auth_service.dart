import '../models/user.dart';

class AuthService {
  Future<AppUser> login(String email, String password) async {
    await Future.delayed(Duration(seconds: 1));
    return AppUser(id: '1', email: email);
  }
}
