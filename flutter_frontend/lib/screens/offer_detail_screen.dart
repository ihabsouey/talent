import 'package:flutter/material.dart';
import '../models/offer.dart';
import '../widgets/custom_button.dart';
import '../constants.dart';

class OfferDetailScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final Offer offer = ModalRoute.of(context)!.settings.arguments as Offer;
    return Scaffold(
      appBar: AppBar(title: Text(offer.title)),
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [lightGradientStart, lightGradientEnd],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
        ),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
            Image.network(
              offer.imageUrl,
              width: double.infinity,
              height: 200,
              fit: BoxFit.cover,
            ),
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(offer.title,
                      style:
                          TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
                  SizedBox(height: 8),
                  Text('${offer.city}, ${offer.country}'),
                  SizedBox(height: 8),
                  Text('Durée: ${offer.duration}'),
                  Text('Rémunération: ${offer.salary}'),
                  Text('Date: ${offer.date}'),
                  SizedBox(height: 16),
                  DefaultTabController(
                    length: 2,
                    child: Column(
                      children: [
                        TabBar(
                          labelColor: primaryColor,
                          tabs: [
                            Tab(text: 'Overview'),
                            Tab(text: 'Details'),
                          ],
                        ),
                        Container(
                          height: 200,
                          child: TabBarView(
                            children: [
                              Padding(
                                padding: const EdgeInsets.all(8.0),
                                child: Text(offer.overview),
                              ),
                              Padding(
                                padding: const EdgeInsets.all(8.0),
                                child: Text(offer.details),
                              )
                            ],
                          ),
                        )
                      ],
                    ),
                  ),
                  SizedBox(height: 16),
                  CustomButton(
                    text: 'Liker ce poste ❤️',
                    onPressed: () {},
                  )
                ],
              ),
            )
          ],
        ),
      ),
    );
  }
}
