INSERT INTO regions (region_name, region_code) VALUES
('Greater Accra', 'GA'),
('Ashanti', 'AS'),
('Northern', 'NR'),
('Western', 'WR'),
('Eastern', 'ER'),
('Central', 'CR'),
('Volta', 'VR'),
('Upper East', 'UER'),
('Upper West', 'UWR'),
('Bono', 'BR'),
('Bono East', 'BER'),
('Ahafo', 'AR'),
('North East', 'NER'),
('Oti', 'OR'),
('Savannah', 'SR'),
('Western North', 'WNR')
ON CONFLICT DO NOTHING;
INSERT INTO districts (district_name, district_code, region_id) VALUES
('Ada East', 'AE', 1),
('Ada West', 'AW', 1),
('Krowor', 'KR', 1),
('La Nkwantanang-Madina', 'LNM', 1),
('Ledzokuku', 'LE', 1)
ON CONFLICT DO NOTHING;