import '../models/offer.dart';

class OfferService {
  Future<List<Offer>> getOffers() async {
    await Future.delayed(Duration(seconds: 2));
    return [
      Offer(
        title: 'DataWave Solutions',
        city: 'Paris',
        country: 'France',
        duration: '6 mois',
        salary: '1000€',
        date: 'Septembre 2026',
        overview: 'Mission principale',
        details: 'Responsabilités, compétences',
        imageUrl:
            'https://images.ctfassets.net/ihx0a8chifpc/gPyHKDGI0md4NkRDjs4k8/36be1e73008a0181c1980f727f29d002/avatar-placeholder-generator-500x500.jpg',
      ),
      Offer(
        title: 'Tech Innovators',
        city: 'Lyon',
        country: 'France',
        duration: '3 mois',
        salary: '800€',
        date: 'Juin 2026',
        overview: 'Découvrir',
        details: 'Apprendre',
        imageUrl:
            'https://images.ctfassets.net/ihx0a8chifpc/gPyHKDGI0md4NkRDjs4k8/36be1e73008a0181c1980f727f29d002/avatar-placeholder-generator-500x500.jpg',
      ),
    ];
  }
}
