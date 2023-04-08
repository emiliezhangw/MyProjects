SELECT * FROM crime_scene_report WHERE date = '20180115' AND city = 'SQL City' AND type = 'murder';
SELECT * FROM person WHERE (address_number = (SELECT MAX(address_number) FROM person WHERE address_street_name = 'Northwestern Dr')) OR name LIKE '%Annabel%' AND address_street_name = 'Franklin Ave';
SELECT * FROM interview WHERE person_id IN (SELECT id FROM person WHERE (address_number = (SELECT MAX(address_number) FROM person WHERE address_street_name = 'Northwestern Dr')) OR name LIKE '%Annabel%' AND address_street_name = 'Franklin Ave');
SELECT * FROM drivers_license WHERE plate_number LIKE "%H42W%" AND gender = 'male';
SELECT * FROM get_fit_now_member WHERE id LIKE '48Z%' AND membership_status = 'gold';
SELECT * FROM person WHERE license_id IN (SELECT id FROM drivers_license WHERE plate_number LIKE "%H42W%" AND gender = 'male');
SELECT * FROM get_fit_now_member WHERE id LIKE '48Z%' AND membership_status = 'gold' AND person_id IN (SELECT id FROM person WHERE license_id IN (SELECT id FROM drivers_license WHERE plate_number LIKE "%H42W%" AND gender = 'male'));

SELECT * FROM person WHERE license_id =
(SELECT id FROM drivers_license WHERE id IN
(SELECT license_id FROM person WHERE id IN
(SELECT person_id FROM facebook_event_checkin WHERE event_name = 'SQL Symphony Concert' AND
date LIKE '201712%' GROUP BY person_id ORDER BY COUNT(*) DESC LIMIT 2)));
