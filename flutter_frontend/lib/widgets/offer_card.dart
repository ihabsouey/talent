import 'package:flutter/material.dart';
import '../models/offer.dart';

class OfferCard extends StatelessWidget {
  final Offer offer;

  const OfferCard({Key? key, required this.offer}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: EdgeInsets.symmetric(vertical: 8),
      child: InkWell(
        onTap: () => Navigator.pushNamed(context, '/detail', arguments: offer),
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Row(
            children: [
              ClipRRect(
                borderRadius: BorderRadius.circular(8),
                child: Image.network(
                  offer.imageUrl,
                  width: 60,
                  height: 60,
                  fit: BoxFit.cover,
                ),
              ),
              SizedBox(width: 16),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(offer.title,
                        style: TextStyle(
                            fontSize: 16, fontWeight: FontWeight.bold)),
                    SizedBox(height: 4),
                    Text('${offer.city}, ${offer.country}'),
                    Text(offer.salary),
                  ],
                ),
              ),
              IconButton(
                icon: Icon(
                  offer.isFavorite ? Icons.favorite : Icons.favorite_border,
                  color: Colors.pink,
                ),
                onPressed: () {},
              )
            ],
          ),
        ),
      ),
    );
  }
}
