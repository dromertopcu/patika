
---

# Ödev 1

## 1. film tablosunda bulunan title ve description sütunlarındaki verileri sıralayınız.

```sql
{
    SELECT title, description FROM film;
}
```

## 2. film tablosunda bulunan tüm sütunlardaki verileri film uzunluğu (length) 60 dan büyük VE 75 ten küçük olma koşullarıyla sıralayınız.

```sql
{
    SELECT * FROM film
    WHERE length > 60 AND length < 75 ;
}
```

## 3. film tablosunda bulunan tüm sütunlardaki verileri rental_rate 0.99 VE replacement_cost 12.99 VEYA 28.99 olma koşullarıyla sıralayınız.

```sql
{
    SELECT * FROM film
    WHERE rental_rate = 0.99 AND replacement_cost IN (12.99,28.99);
}
```

## 4. customer tablosunda bulunan first_name sütunundaki değeri 'Mary' olan müşterinin last_name sütunundaki değeri nedir?

```sql
{
    SELECT last_name FROM customer
    WHERE first_name = 'Mary';
}
```

## 5. film tablosundaki uzunluğu(length) 50 ten büyük OLMAYIP aynı zamanda rental_rate değeri 2.99 veya 4.99 OLMAYAN verileri sıralayınız.

```sql
{
    SELECT * FROM film
    WHERE NOT length > 50 AND rental_rate NOT IN (2.99,4.99);
}
```

---

---

# Ödev 2

## 1. film tablosunda bulunan tüm sütunlardaki verileri replacement cost değeri 12.99 dan büyük eşit ve 16.99 küçük olma koşuluyla sıralayınız ( BETWEEN - AND yapısını kullanınız.)

```sql
{
    SELECT * FROM film
    WHERE replacement_cost BETWEEN 12.99 AND 16.99;
}
```

## 2. actor tablosunda bulunan first_name ve last_name sütunlardaki verileri first_name 'Penelope' veya 'Nick' veya 'Ed' değerleri olması koşuluyla sıralayınız. ( IN operatörünü kullanınız.)

```sql
{
    SELECT first_name, last_name FROM actor
    WHERE first_name IN ('Penelope','Nick','Ed');
}
```

## 3. film tablosunda bulunan tüm sütunlardaki verileri rental_rate 0.99, 2.99, 4.99 VE replacement_cost 12.99, 15.99, 28.99 olma koşullarıyla sıralayınız. ( IN operatörünü kullanınız.)

```sql
{
    SELECT * FROM film
    WHERE rental_rate IN (0.99,2.99,4.99) AND replacement_cost IN (12.99,15.99,28.99);
}
```

---

---

# Ödev 3

## 1. country tablosunda bulunan country sütunundaki ülke isimlerinden 'A' karakteri ile başlayıp 'a' karakteri ile sonlananları sıralayınız.

```sql
{
    SELECT country FROM country
    WHERE country LIKE 'A%a';
}
```

## 2. country tablosunda bulunan country sütunundaki ülke isimlerinden en az 6 karakterden oluşan ve sonu 'n' karakteri ile sonlananları sıralayınız.

```sql
{
    SELECT country FROM country
    WHERE country LIKE '_____n';
}
```

## 3. film tablosunda bulunan title sütunundaki film isimlerinden en az 4 adet büyük ya da küçük harf farketmesizin 'T' karakteri içeren film isimlerini sıralayınız.

```sql
{
    SELECT title FROM film
    WHERE title ILIKE '%t%t%t%t%';
}
```

## 4. film tablosunda bulunan tüm sütunlardaki verilerden title 'C' karakteri ile başlayan ve uzunluğu (length) 90 dan büyük olan ve rental_rate 2.99 olan verileri sıralayınız.

```sql
{
    SELECT * FROM film
    WHERE title LIKE 'C%' AND length > 90 AND rental_rate = 2.99;
}
```

---

---

# Ödev 4

## 1. film tablosunda bulunan replacement_cost sütununda bulunan birbirinden farklı değerleri sıralayınız.

```sql
{
     DISTINCT replacement_cost FROM film;
}
```

## 2. film tablosunda bulunan replacement_cost sütununda birbirinden farklı kaç tane veri vardır?

```sql
{
    NT(DISTINCT replacement_cost) FROM film;
}
```

## 3. film tablosunda bulunan film isimlerinde (title) kaç tanesini T karakteri ile başlar ve aynı zamanda rating 'G' ye eşittir?

```sql
{
    SELECT COUNT(*) FROM film
    WHERE title LIKE 'T%' AND rating = 'G';
}
```

## 4. country tablosunda bulunan ülke isimlerinden (country) kaç tanesi 5 karakterden oluşmaktadır?

```sql
{
    SELECT COUNT(*) FROM country
    WHERE country LIKE '_____';
}
```

## 5. city tablosundaki şehir isimlerinin kaç tanesi 'R' veya r karakteri ile biter?

```sql
{
    SELECT COUNT(*) FROM city
    WHERE city ILIKE '%r';
}
```

---

---

# Ödev 5

## 1. film tablosunda bulunan ve film ismi (title) 'n' karakteri ile biten en uzun (length) 5 filmi sıralayınız.

```sql
{
    SELECT * FROM film
    WHERE title LIKE '%n'
    ORDER BY length DESC
    LIMIT 5;
}
```

## 2. film tablosunda bulunan ve film ismi (title) 'n' karakteri ile biten en kısa (length) ikinci(6,7,8,9,10) 5 filmi(6,7,8,9,10) sıralayınız.

```sql
{
    SELECT * FROM film
    WHERE title LIKE '%n'
    ORDER BY length
    OFFSET 5
    LIMIT 5;
}
```

## 3. customer tablosunda bulunan last_name sütununa göre azalan yapılan sıralamada store_id 1 olmak koşuluyla ilk 4 veriyi sıralayınız.

```sql
{
    SELECT * FROM customer
    WHERE store_id = 1
    ORDER BY last_name DESC
    LIMIT 4;
}
```

---

---

# Ödev 6

## 1. film tablosunda bulunan rental_rate sütunundaki değerlerin ortalaması nedir?

```sql
{
    SELECT AVG(rental_rate) FROM film;
}
```

## 2. film tablosunda bulunan filmlerden kaç tanesi 'C' karakteri ile başlar?

```sql
{
    SELECT COUNT(*) FROM film
    WHERE title LIKE 'C%';
}
```

## 3. film tablosunda bulunan filmlerden rental_rate değeri 0.99 a eşit olan en uzun (length) film kaç dakikadır?

```sql
{
    SELECT length FROM film
    WHERE rental_rate = 0.99
    ORDER BY length DESC
    LIMIT 1;
}
```

## 4. film tablosunda bulunan filmlerin uzunluğu 150 dakikadan büyük olanlarına ait kaç farklı replacement_cost değeri vardır?

```sql
{
    SELECT COUNT(DISTINCT replacement_cost) FROM film
    WHERE length > 150;
}
```

---

---

# Ödev 7

## 1. film tablosunda bulunan filmleri rating değerlerine göre gruplayınız.

```sql
{
    SELECT rating, COUNT(rating) FROM film
    GROUP BY rating;
}
```

## 2. film tablosunda bulunan filmleri replacement_cost sütununa göre grupladığımızda film sayısı 50 den fazla olan replacement_cost değerini ve karşılık gelen film sayısını sıralayınız.

```sql
{
    SELECT replacement_cost, COUNT(replacement_cost) FROM film
    GROUP BY replacement_cost
    HAVING COUNT(replacement_cost) > 50;
}
```

## 3. customer tablosunda bulunan store_id değerlerine karşılık gelen müşteri sayılarını nelerdir?

```sql
{
    SELECT store_id, COUNT(store_id) FROM customer
    GROUP BY store_id;
}
```

## 4. city tablosunda bulunan şehir verilerini country_id sütununa göre gruplandırdıktan sonra en fazla şehir sayısı barındıran country_id bilgisini ve şehir sayısını paylaşınız.

```sql
{
    SELECT country_id, COUNT(country_id) FROM city
    GROUP BY country_id
    ORDER BY COUNT(country_id)
    LIMIT 1;
}
```

---

---

# Ödev 8

## 1. test veritabanınızda employee isimli sütun bilgileri id(INTEGER), name VARCHAR(50), birthday DATE, email VARCHAR(100) olan bir tablo oluşturalım.

```sql
{
    CREATE TABLE employee (
        id INTEGER,
        name VARCHAR(50),
        birthday DATE,
        email VARCHAR(100)
    );
}
```

## 2. Oluşturduğumuz employee tablosuna 'Mockaroo' servisini kullanarak 50 adet veri ekleyelim.

```sql
{
    INSERT INTO employee (id, name, birthday, email)
    VALUES (1, 'Morrie Menendez', '1970-12-23','mmenendez0@example.com'),
    (2,'Esta Lubman','1989-10-12','elubman1@printfriendly.com');
}
```

## 3. Sütunların her birine göre diğer sütunları güncelleyecek 5 adet UPDATE işlemi yapalım.

```sql
{
    UPDATE employee
    SET name = 'UPDATED'
    WHERE id % 3 = 0;
}
```

## 4. Sütunların her birine göre ilgili satırı silecek 5 adet DELETE işlemi yapalım.

```sql
{
    DELETE FROM employee
    WHERE birthday < '1975-01-01';
}
```

---

---

# Ödev 9

## 1. city tablosu ile country tablosunda bulunan şehir (city) ve ülke (country) isimlerini birlikte görebileceğimiz INNER JOIN sorgusunu yazınız.

```sql
{
SELECT city, country FROM city
INNER JOIN country ON city.country_id = country.country_id;
}
```

## 2. customer tablosu ile payment tablosunda bulunan payment_id ile customer tablosundaki first_name ve last_name isimlerini birlikte görebileceğimiz INNER JOIN sorgusunu yazınız.

```sql
{
SELECT payment_id, first_name, last_name FROM customer
INNER JOIN payment ON customer.customer_id = payment.customer_id;
}
```

## 3. customer tablosu ile rental tablosunda bulunan rental_id ile customer tablosundaki first_name ve last_name isimlerini birlikte görebileceğimiz INNER JOIN sorgusunu yazınız.

```sql
{
SELECT rental_id, first_name, last_name FROM customer
INNER JOIN rental ON customer.customer_id = rental.customer_id;
}
```

---

---

# Ödev 10

## 1. city tablosu ile country tablosunda bulunan şehir (city) ve ülke (country) isimlerini birlikte görebileceğimiz LEFT JOIN sorgusunu yazınız.

```sql
{
SELECT city.city, country.country FROM city
LEFT JOIN country ON city.country_id = country.country_id;
}
```

## 2. customer tablosu ile payment tablosunda bulunan payment_id ile customer tablosundaki first_name ve last_name isimlerini birlikte görebileceğimiz RIGHT JOIN sorgusunu yazınız.

```sql
{
SELECT payment.payment_id, customer.first_name, customer.last_name FROM customer
RIGHT JOIN payment ON payment.customer_id = customer.customer_id;
}
```

## 3. customer tablosu ile rental tablosunda bulunan rental_id ile customer tablosundaki first_name ve last_name isimlerini birlikte görebileceğimiz FULL JOIN sorgusunu yazınız.

```sql
{
SELECT rental.rental_id, customer.first_name, customer.last_name FROM customer
FULL JOIN rental ON rental.customer_id = customer.customer_id;
}
```

---

---

# Ödev 11

## 1. actor ve customer tablolarında bulunan first_name sütunları için tüm verileri sıralayalım.

```sql
{
SELECT first_name FROM actor
UNION
SELECT first_name FROM customer;
}
```

## 2. actor ve customer tablolarında bulunan first_name sütunları için kesişen verileri sıralayalım.

```sql
{
SELECT first_name FROM actor
INTERSECT
SELECT first_name FROM customer;
}
```

## 3. actor ve customer tablolarında bulunan first_name sütunları için ilk tabloda bulunan ancak ikinci tabloda bulunmayan verileri sıralayalım.

```sql
{
SELECT first_name FROM actor
EXCEPT
SELECT first_name FROM customer;
}
```

## 4. İlk 3 sorguyu tekrar eden veriler için de yapalım.

```sql
{
1. UNION ALL;
2. INTERSECT ALL;
3. EXCEPT ALL;
}
```

---

---

# Ödev 12

## 1. film tablosunda film uzunluğu length sütununda gösterilmektedir. Uzunluğu ortalama film uzunluğundan fazla kaç tane film vardır?

```sql
{
SELECT COUNT(*) FROM film
WHERE length > 
(
SELECT AVG(length) FROM film
);
}
```

## 2. film tablosunda en yüksek rental_rate değerine sahip kaç tane film vardır?

```sql
{
SELECT COUNT(*) FROM film
WHERE rental_rate = 
(
SELECT MAX(rental_rate) FROM film
);
}
```

## 3. film tablosunda en düşük rental_rate ve en düşün replacement_cost değerlerine sahip filmleri sıralayınız.

```sql
{
SELECT title, rental_rate, replacement_cost
FROM film
WHERE rental_rate = 
	(
		SELECT MIN(rental_rate) FROM film
	) 
AND 
	replacement_cost =
	(
		SELECT MIN(replacement_cost) FROM film
	);
}
```

## 4. payment tablosunda en fazla sayıda alışveriş yapan müşterileri(customer) sıralayınız.

```sql
{
SELECT COUNT(payment.customer_id), customer.first_name, customer.last_name, payment.customer_id AS id
FROM payment
JOIN customer ON customer.customer_id = payment.customer_id
GROUP BY payment.customer_id, customer.first_name, customer.last_name
ORDER BY COUNT(payment.customer_id) DESC;
}
```

---
