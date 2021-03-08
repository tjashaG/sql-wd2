from smartninja_sql.sqlite import SQLiteDatabase

if __name__ == "__main__":

    db = SQLiteDatabase("Chinook_Sqlite (1).sqlite")
    db.print_tables(verbose=True)

    # What order (Invoice) was the most expensive? Which one was the cheapest?

    most_expensive_order = db.execute("SELECT MAX(Total) FROM Invoice;")
    print(f"The most expensive order is: {most_expensive_order}")
    # 25.86

    cheapest_order = db.execute("SELECT MIN(Total) FROM Invoice;")
    print(f"The cheapest order is: {cheapest_order}")
    # 0.99

    # Which city (BillingCity) has the most orders?

    city_with_most_orders = db.execute("""SELECT COUNT(BillingCity), BillingCity
                                          FROM Invoice
                                          GROUP BY BillingCity
                                          ORDER BY COUNT(BillingCity) DESC
                                          LIMIT 6;
                                          """)
    print("Cities with most orders are: ")
    for city in city_with_most_orders:
        print(city)

    # (14, 'São Paulo')
    # (14, 'Prague')
    # (14, 'Paris')
    # (14, 'Mountain View')
    # (14, 'London')
    # (14, 'Berlin')
    # Could just print entire list, couldn't figure out, how to get JUST the highest value ones

    # Calculate (or count) how many tracks have this MediaType: Protected AAC audio file.

    media_type = db.execute("""SELECT COUNT(Track.Name) FROM Track
                                JOIN MediaType ON MediaType.MediaTypeId = Track.MediaTypeId
                                WHERE MediaType.Name = 'Protected AAC audio file';
                                """)

    print(f"Number of tracks with Media Type 'Protected AAC audio file': {media_type}")
    # 237

    media_type2 = db.execute("""SELECT COUNT(Name) FROM Track
                                WHERE MediaTypeId IN
                                (SELECT MediaTypeId FROM MediaType WHERE Name = 'Protected AAC audio file');
                                """)

    # print(media_type2)
    # 237

    # Find out what Artist has the most albums?

    most_albums_by_artist = db.execute("""SELECT COUNT(Album.Title), Artist.Name 
                                            FROM Album
                                            JOIN Artist ON Album.ArtistId = Artist.ArtistId
                                            GROUP BY Artist.Name
                                            ORDER BY COUNT(Album.Title) DESC
                                            LIMIT 1;
                                         """)

    print(f"The artist {most_albums_by_artist[0][1]} has the most albums: {most_albums_by_artist[0][0]}")
    # (21, 'Iron Maiden')

    # What genre has the most tracks?

    most_tracks_by_genre = db.execute("""SELECT COUNT(Track.Name), Genre.Name FROM Track
                                         JOIN Genre ON Track.GenreId = Genre.GenreId
                                         GROUP BY Genre.Name
                                         ORDER BY COUNT(Track.Name) DESC
                                         LIMIT 1;
                                        """)
    print(f"The genre {most_tracks_by_genre[0][1]} has the most tracks: {most_tracks_by_genre[0][0]}")
    # (1297, 'Rock')

    # Which customer spent the most money so far?

    biggest_spender = db.execute("""SELECT Customer.FirstName, Customer.LastName, SUM(Invoice.Total)
                                    FROM Customer
                                    JOIN Invoice ON Invoice.CustomerId = Customer.CustomerId
                                    GROUP BY Invoice.CustomerId
                                    ORDER BY SUM(Invoice.Total) DESC
                                    LIMIT 1;
                                    """)
    print(f"Our biggest spender is {biggest_spender[0][0] + ' ' + biggest_spender[0][1]} with {biggest_spender[0][2]} spent")
    # ('Helena', 'Holý', 49.620000000000005)

    # What songs were bought with each order?

    order_and_song = db.execute("""SELECT InvoiceLine.InvoiceId, Track.Name
                                    FROM InvoiceLine
                                    JOIN Invoice ON Invoice.InvoiceId = InvoiceLine.InvoiceId
                                    JOIN Track ON Track.TrackId = InvoiceLine.TrackId;
                                """)
    #for song in order_and_song:
     #   print(song)

    # print all the tracks with corresponding artist and album

    aat = db.execute("""SELECT Track.Name, Artist.Name, Album.Title
                        FROM Track
                        JOIN Album ON Track.AlbumId = Album.AlbumId
                        JOIN Artist ON Artist.ArtistId = Album.ArtistId
                        ORDER BY Artist.Name;
    
    """)

    #for a in aat:
     #   print(a)

