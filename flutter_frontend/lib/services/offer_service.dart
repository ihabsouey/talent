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
        imageUrl: 'https://via.placeholder.com/150',
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
        imageUrl: 'https://via.placeholder.com/150',
      ),
    ];
  }
}
