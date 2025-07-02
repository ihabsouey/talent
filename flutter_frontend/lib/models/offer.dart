class Offer {
  final String title;
  final String city;
  final String country;
  final String duration;
  final String salary;
  final String date;
  final String overview;
  final String details;
  final String imageUrl;
  bool isFavorite;

  Offer({
    required this.title,
    required this.city,
    required this.country,
    required this.duration,
    required this.salary,
    required this.date,
    required this.overview,
    required this.details,
    required this.imageUrl,
    this.isFavorite = false,
  });
}
