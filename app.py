from flask import Flask, request, render_template, redirect, jsonify


medicine_json = [
{
"type": "drug",
"display_text": "Crocin 120 Suspension (Strawberry Flavor)",
"mds_id": "7d3237d7-9e71-4481-af5a-92cb929709e3",
"drug": {
"regulatory_class_id": "1083d4e0-7591-4602-b230-82086f77f287",
"regulatory_class_name": "OTC",
"requires_prescription": False,
"productId": "d75be199-95c2-4feb-8b2f-a437830de233",
"product_name": "Paracetamol (120 mg/5 ml) Suspension",
"dosage_form_id": "313157aa-2efc-4a54-ab41-67b1ae9b0c73",
"dosage_form_name": "Suspension",
"brand_id": "7d3237d7-9e71-4481-af5a-92cb929709e3",
"brand_name": "Crocin 120 Suspension (Strawberry Flavor)",
"manufacturer_id": "645b79d4-accc-4c4e-a1b2-65e54188ec60",
"manufacturer_name": "Glaxosmithkline Pharmaceuticals Ltd.",
"slug": "crocin-125-mg-suspension-3275",
"pp_enabled": True,
"order_enabled": True,
"quantity_per_pack": 1,
"sub_type": "drug",
"type": "drug",
"indication_name": [
"Fever",
"Headache",
"Muscle Pain",
"Post Immunization Pyrexia"
],
"composition_name": "Paracetamol",
"result_type": "exact",
"is_available": True,
"mrp": 33.34,
"discount": 15,
"dose_id": 605054,
"pack_name": "60ML",
"pack_type": "BOTTLE",
"pack": "60ML",
"pack_content_type": "LIQUID",
"pack_info": "60ml Liquid",
"images": [
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/0f2933bef3610b4f478d56e34d288c0892269b461.jpg",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/0f2933bef3610b4f478d56e34d288c0892269b461.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/1877d81414ce213efaf38b99ba7622c608dabe271_cropped_not_compressed.JPG"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/c6b5e1fae3e9faebecad0cdadac100938ed6d2f92_cropped_not_compressed.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/add95d66d9a7546c66f0503bd42a9b506fa8ad102.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/3b466438892afd50e54b66b81f190219a7bd622e2.JPG"
},
{
"res-750": "https://www.practostatic.com/practopedia-images/res-750/0677580912e935fa9b944a1c5f88b45b573f19853.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/a6efe3a08c536a94169bc64b2c54326ddcb55c2a3_cropped_not_compressed.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/2adb6918f70677a96767fdd0f44c8aee33157e1e3.JPG"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/af3aedf2ac61c5fb3623689d543dd6212b7864f44.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/caa01ae0181ac04b3b8f460d3249daf8d1c119024.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/cfdf4ad2990e3dbb15a689bd15a48334bc0864b54_cropped_not_compressed.JPG"
},
{
"res-750": "https://www.practostatic.com/practopedia-images/res-750/fff2371da0466be158b9dffc0fc1628c727ac9f15.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/0a812435eacada9c16377e5f6b01cc4033ac9aae5.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/74979624650f59719951df029a7e785cc1d9599c5_cropped_not_compressed.JPG"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/f240ceafb7491db788e29a98b46d0be48937c4686_cropped_not_compressed.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/682f0ad4a4c0b37c536fe1ab9989dbc8b6017f466.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/a059a5ae1816712e9b88da3ddfd18aaf36d9c96e6.JPG"
}
]
}
},
{
"type": "drug",
"display_text": "Crocin Baby (Peppermint Flavour) Drops",
"mds_id": "628fed02-2b45-48da-a39f-a5c960374b5c",
"drug": {
"regulatory_class_id": "1083d4e0-7591-4602-b230-82086f77f287",
"regulatory_class_name": "OTC",
"requires_prescription": False,
"productId": "e2d149b5-33e6-41a2-b5f9-79a3955d07ea",
"product_name": "Paracetamol (100 mg/ml) Oral Drops",
"dosage_form_id": "310b8192-0be3-486a-8599-d9b7f39422d3",
"dosage_form_name": "Oral Drops",
"brand_id": "628fed02-2b45-48da-a39f-a5c960374b5c",
"brand_name": "Crocin Baby (Peppermint Flavour) Drops",
"manufacturer_id": "645b79d4-accc-4c4e-a1b2-65e54188ec60",
"manufacturer_name": "Glaxosmithkline Pharmaceuticals Ltd.",
"slug": "crocin-150-mg-drops-3276",
"pp_enabled": True,
"order_enabled": True,
"quantity_per_pack": 1,
"sub_type": "drug",
"type": "drug",
"indication_name": [
"Fever",
"Headache",
"Muscle Pain",
"Post Immunization Pyrexia"
],
"composition_name": "Paracetamol",
"result_type": "exact",
"is_available": True,
"mrp": 25.53,
"discount": 0,
"dose_id": 123753,
"pack_name": "15ML",
"pack_type": "DROPS",
"pack": "15ML",
"pack_content_type": "ORAL DROPS",
"pack_info": "15ml Oral Drops",
"images": [
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/cdc9aeef566254575b8598ebfabb92b62b78b6d01.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/c2fbc218664da09e88a629cd35495415ea04f1401.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/253ed50db3140b541e3bd558bf0abbc834ef668d1_cropped_not_compressed.JPG"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/7e4253983a0c4dd658dd95bc6c3f5d96e5e001d92.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/a30985db6baf2503134e7f2566ecb4b1a89088de2.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/a204675692fb2926b36ac40cb905eb8a172fb3872_cropped_not_compressed.JPG"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/8386a7f280df295831815e7493d7644972ea05ce3.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/8386a7f280df295831815e7493d7644972ea05ce3.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/d97f56145ebf13432ab1f323cc885d248388f01e3_cropped_not_compressed.JPG"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/a6c00ab736610dc9cd4b8de7f37ebe3b20f0bd6f4.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/a6c00ab736610dc9cd4b8de7f37ebe3b20f0bd6f4.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/fafd67cd32d653cb5a6dcd012e7d72d3d86d5de14_cropped_not_compressed.JPG"
}
]
}
},
{
"type": "drug",
"display_text": "Crocin 650 Tablet",
"mds_id": "7332fa9b-020f-430a-b098-9545756eda91",
"drug": {
"regulatory_class_id": "1083d4e0-7591-4602-b230-82086f77f287",
"regulatory_class_name": "OTC",
"requires_prescription": False,
"productId": "d1276630-e1b0-42fd-921e-bd20c183d18c",
"product_name": "Paracetamol (650 mg) Tablet",
"dosage_form_id": "94e616e3-f7cf-4a0c-a922-05ce398804fd",
"dosage_form_name": "Tablet",
"brand_id": "7332fa9b-020f-430a-b098-9545756eda91",
"brand_name": "Crocin 650 Tablet",
"manufacturer_id": "645b79d4-accc-4c4e-a1b2-65e54188ec60",
"manufacturer_name": "Glaxosmithkline Pharmaceuticals Ltd.",
"slug": "crocin-650-mg-tablet-3279",
"pp_enabled": True,
"order_enabled": True,
"quantity_per_pack": 15,
"sub_type": "drug",
"type": "drug",
"indication_name": [
"Fever",
"Headache",
"Muscle Pain",
"Menstrual Cramps",
"Post Immunization Pyrexia",
"Arthritis"
],
"composition_name": "Paracetamol",
"result_type": "exact",
"is_available": False,
"mrp": 28.9995,
"discount": 0,
"dose_id": 487922,
"pack_name": "15`S",
"pack_type": "STRIPS",
"pack": 15,
"pack_content_type": "TABLET",
"pack_info": "15 Tablet ( 15 / Strip )",
"images": [
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/7d15abc42ec9af322412ee19a2ee0938ad41fd531.jpg",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/3901c37217886184d948833f67284ebd32f8ea131.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/c75cbd731d961e84aa0f64109f9aac4848009fad1_cropped_not_compressed.JPG"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/23b229b5ac4d1ad99efcbd141fb59763fc01705e2_cropped_not_compressed.jpg",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/158cfae73a01092d583de5257a1b02138d88220f2.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/158cfae73a01092d583de5257a1b02138d88220f2.jpg"
},
{
"res-750": "https://www.practostatic.com/practopedia-images/res-750/950c0f0614883d28e878d1db98b5341e5126c66d3.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/950c0f0614883d28e878d1db98b5341e5126c66d3.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/ea6b5d93dae90d90b798ba2c5e2efc9a9218a2543_cropped_not_compressed.JPG"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/311fac62ae02df4073162fb4b813a6665a641f564_cropped_not_compressed.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/f53e08f30cd4475fcb8d43aecc0cff776ad7f18b4.jpg",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/f53e08f30cd4475fcb8d43aecc0cff776ad7f18b4.jpg"
}
]
}
},
{
"type": "drug",
"display_text": "Crocin Pain Relief Tablet",
"mds_id": "472a3734-0614-4e53-bcbb-2c80a3cca1c8",
"drug": {
"regulatory_class_id": "4e0889e5-3859-4129-8fff-7a14a417ee38",
"regulatory_class_name": "Schedule G",
"requires_prescription": True,
"productId": "0fd4f7f2-f67a-419e-958b-eeec95ccf6e1",
"product_name": "Paracetamol (650 mg) + Caffeine (50 mg) Tablet",
"dosage_form_id": "94e616e3-f7cf-4a0c-a922-05ce398804fd",
"dosage_form_name": "Tablet",
"brand_id": "472a3734-0614-4e53-bcbb-2c80a3cca1c8",
"brand_name": "Crocin Pain Relief Tablet",
"manufacturer_id": "645b79d4-accc-4c4e-a1b2-65e54188ec60",
"manufacturer_name": "Glaxosmithkline Pharmaceuticals Ltd.",
"slug": None,
"pp_enabled": False,
"order_enabled": True,
"quantity_per_pack": 15,
"sub_type": "drug",
"type": "drug",
"result_type": "exact",
"is_available": True,
"mrp": 59.7,
"discount": 15,
"dose_id": 123763,
"pack_name": "15`S",
"pack_type": "STRIPS",
"pack": 15,
"pack_content_type": "TABLET",
"pack_info": "15 Tablet ( 15 / Strip )",
"images": [
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/9f81da7a1e6218a915afddb0839657f6b96b36fd1.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/9f81da7a1e6218a915afddb0839657f6b96b36fd1.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/79843b7221f658313fec84d82da9bdbf5e9555f11_cropped_not_compressed.JPG"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/81aadd3edfb09636974dd5d7d8ed43e4a05770c92.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/c74e6bd83cf7aad67f189a4f81e2427871868f6d2.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/1db813947fb7838e8c8fb17c7331a4f15c8b0bb82_cropped_not_compressed.JPG"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/b9559be5e77f438448127b9a1d65fd48f97275a13_cropped_not_compressed.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/3f2fd2ead6cc8031b8d941f68d0672cf4ebb22b53.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/3f2fd2ead6cc8031b8d941f68d0672cf4ebb22b53.JPG"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/185dd03f6c8208b3cfc6531d1c3f61570b476a4e4.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/5ec4a163c4d09155171905106794d79882d1f5024.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/767c8e3e3fa7b428e5a14e31ab5c2eff561ec4e64_cropped_not_compressed.JPG"
}
]
}
},
{
"type": "drug",
"display_text": "Crocin Advance Tablet",
"mds_id": "ec9e4518-ed38-4217-b7e2-29b7684df642",
"drug": {
"regulatory_class_id": "1083d4e0-7591-4602-b230-82086f77f287",
"regulatory_class_name": "OTC",
"requires_prescription": False,
"productId": "501794d7-a96a-422f-afef-d55be11a2c9e",
"product_name": "PARACETAMOL (500 mg) Tablet",
"dosage_form_id": "94e616e3-f7cf-4a0c-a922-05ce398804fd",
"dosage_form_name": "Tablet",
"brand_id": "ec9e4518-ed38-4217-b7e2-29b7684df642",
"brand_name": "CROCIN ADVANCE TABLET",
"manufacturer_id": "645b79d4-accc-4c4e-a1b2-65e54188ec60",
"manufacturer_name": "Glaxosmithkline Pharmaceuticals Ltd.",
"slug": "crocin-advance-500-mg-tablet-3278",
"pp_enabled": True,
"order_enabled": False,
"quantity_per_pack": None,
"sub_type": "drug",
"type": "drug",
"indication_name": [
"Fever",
"Headache",
"Muscle Pain",
"Menstrual Cramps",
"Post Immunization Pyrexia",
"Arthritis"
],
"composition_name": "Paracetamol",
"result_type": "exact",
"is_available": False
}
},
{
"type": "drug",
"display_text": "Crocin 1000 Mg Tablet",
"mds_id": "ed58aad0-af92-4969-ab13-0c9acea555a9",
"drug": {
"regulatory_class_id": "1083d4e0-7591-4602-b230-82086f77f287",
"regulatory_class_name": "OTC",
"requires_prescription": False,
"productId": "b01615b4-2caa-406c-8377-c732abe43e14",
"product_name": "Paracetamol (1000 mg) Tablet",
"dosage_form_id": "94e616e3-f7cf-4a0c-a922-05ce398804fd",
"dosage_form_name": "Tablet",
"brand_id": "ed58aad0-af92-4969-ab13-0c9acea555a9",
"brand_name": "CROCIN 1000 mg TABLET",
"manufacturer_id": "645b79d4-accc-4c4e-a1b2-65e54188ec60",
"manufacturer_name": "Glaxosmithkline Pharmaceuticals Ltd.",
"slug": "crocin-1000-mg-tablet-3274",
"pp_enabled": True,
"order_enabled": False,
"quantity_per_pack": None,
"sub_type": "drug",
"type": "drug",
"indication_name": [
"Fever",
"Headache",
"Muscle Pain",
"Menstrual Cramps",
"Post Immunization Pyrexia",
"Arthritis"
],
"composition_name": "Paracetamol",
"result_type": "exact",
"is_available": False
}
},
{
"type": "drug",
"display_text": "Crocin 240 Ds Mixed Fruit Suspension",
"mds_id": "3fc3d1a7-157a-468d-be99-26c714460bc5",
"drug": {
"regulatory_class_id": "1083d4e0-7591-4602-b230-82086f77f287",
"regulatory_class_name": "OTC",
"requires_prescription": False,
"productId": "a8e7f480-2e59-4c18-b46b-b2024f2ce89c",
"product_name": "Paracetamol (240 mg) Suspension",
"dosage_form_id": "313157aa-2efc-4a54-ab41-67b1ae9b0c73",
"dosage_form_name": "Suspension",
"brand_id": "3fc3d1a7-157a-468d-be99-26c714460bc5",
"brand_name": "Crocin 240 DS Mixed Fruit Suspension",
"manufacturer_id": "645b79d4-accc-4c4e-a1b2-65e54188ec60",
"manufacturer_name": "Glaxosmithkline Pharmaceuticals Ltd.",
"slug": "crocin-240-mg-suspension-3277",
"pp_enabled": True,
"order_enabled": False,
"quantity_per_pack": None,
"sub_type": "drug",
"type": "drug",
"indication_name": [
"Fever",
"Headache",
"Muscle Pain",
"Post Immunization Pyrexia"
],
"composition_name": "Paracetamol",
"result_type": "exact",
"is_available": False
}
},
{
"type": "drug",
"display_text": "Corcium Tablet",
"mds_id": "b4edcde6-32c5-4603-84d6-888b7ee53820",
"drug": {
"regulatory_class_id": "4e0889e5-3859-4129-8fff-7a14a417ee38",
"regulatory_class_name": "Schedule G",
"requires_prescription": True,
"productId": "7d0e76c8-ef3c-43cb-896a-2e8e064dff65",
"product_name": "Calcium (225 mg) Tablet",
"dosage_form_id": "94e616e3-f7cf-4a0c-a922-05ce398804fd",
"dosage_form_name": "Tablet",
"brand_id": "b4edcde6-32c5-4603-84d6-888b7ee53820",
"brand_name": "CORCIUM TABLET",
"manufacturer_id": "aa5ad259-19e7-4a5d-87ae-7699c3d74d35",
"manufacturer_name": "Lupin Ltd.",
"slug": None,
"pp_enabled": False,
"order_enabled": True,
"quantity_per_pack": 10,
"sub_type": "drug",
"type": "drug",
"result_type": "fuzzy",
"is_available": True,
"mrp": 96,
"discount": 15,
"dose_id": 122974,
"pack_name": "10`S",
"pack_type": "STRIPS",
"pack": 10,
"pack_content_type": "TABLET",
"pack_info": "10 Tablet ( 10 / Strip )",
"images": [
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/1266317aa08165f079d75a1a82bb4dc84fe159271_cropped_not_compressed.jpg",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/a03cd140deee4e1c7b977d051143c5d260faae431.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/4a390edefaa84c98f6d9ac96d7e466c1dc4fd25b1.jpg"
},
{
"res-750": "https://www.practostatic.com/practopedia-images/res-750/0a27afc2e22bca01fc1e7b3c1e42c1d37574494c2.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/0a27afc2e22bca01fc1e7b3c1e42c1d37574494c2.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/5e9b9c862b6a11bd830d0139e1eb9ed2e5f85f932_cropped_not_compressed.JPG"
},
{
"res-750": "https://www.practostatic.com/practopedia-images/res-750/87998d2ad4084c68f60ebc62b58bb133b30fa36c3.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/87998d2ad4084c68f60ebc62b58bb133b30fa36c3.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/c78acd3d97f53c811681fff24d1a081ef86fc2d53_cropped_not_compressed.JPG"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/7ef7cd1577f0bf37a9e9f0b656a2c3da8e78d8854_cropped_not_compressed.JPG"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/e12df441f8320ff43d9ac45935bb430df3de31505_cropped_not_compressed.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/23c9364bdb29c66e750e5952c66b31b211f579665.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/3f6c2ccce57503578430fb5f1e5f1cd495a35e895.jpg"
},
{
"res-750": "https://www.practostatic.com/practopedia-images/res-750/7ed4061aed3914cba53948dede107f6e541fbce46.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/690d91b22a0b79485b7ea9f817d8e1e885aa9bbc6.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/7c5c8ec13dfcd2186cf423507f69f2d0d9d03e3a6_cropped_not_compressed.JPG"
}
]
}
},
{
"type": "drug",
"display_text": "Crolim 0.03 % Ointment",
"mds_id": "fe73153f-c710-4846-ae1f-6925a7960751",
"drug": {
"regulatory_class_id": "4e0889e5-3859-4129-8fff-7a14a417ee38",
"regulatory_class_name": "Schedule G",
"requires_prescription": True,
"productId": "06400734-443e-42a0-9233-12dd85b83cfb",
"product_name": "Tacrolimus (0.03 %) Ointment",
"dosage_form_id": "f7bc6f40-d8e8-411b-8a2b-9fc2f2b7ee1f",
"dosage_form_name": "Ointment",
"brand_id": "fe73153f-c710-4846-ae1f-6925a7960751",
"brand_name": "CROLIM 0.03 % OINTMENT",
"manufacturer_id": "5da5431b-a4fe-45c1-b601-29c899ee550d",
"manufacturer_name": "Sun Pharma Laboratories Ltd.",
"slug": "crolim-003-ointment-23373",
"pp_enabled": True,
"order_enabled": True,
"quantity_per_pack": 1,
"sub_type": "drug",
"type": "drug",
"indication_name": [
"Organ Transplant - Rejection Prophylaxis"
],
"composition_name": "Tacrolimus",
"result_type": "fuzzy",
"is_available": True,
"mrp": 235,
"discount": 15,
"dose_id": 243252,
"pack_name": "15GM",
"pack_type": "TUBE",
"pack": "15GM",
"pack_content_type": "OINTMENT",
"pack_info": "15gm Ointment"
}
},
{
"type": "drug",
"display_text": "Corcium D3 Tablet",
"mds_id": "eb921028-5345-4126-ad93-1858b3256617",
"drug": {
"brand_id": "eb921028-5345-4126-ad93-1858b3256617",
"brand_name": "CORCIUM D3 TABLET",
"product_name": None,
"regulatory_class_id": "8cbd390e-e850-4aab-abb9-f8f7925d21f0",
"regulatory_class_name": "Nutraceuticals",
"dosage_form_id": "06513c41-2efe-4668-af90-84e410cae32b",
"dosage_form_name": "Tablet",
"requires_prescription": False,
"pp_enabled": False,
"sub_type": "general_product",
"type": "drug",
"order_enabled": True,
"quantity_per_pack": 10,
"manufacturer_id": "aa5ad259-19e7-4a5d-87ae-7699c3d74d35",
"manufacturer_name": "Lupin Ltd.",
"result_type": "fuzzy",
"is_available": True,
"mrp": 132,
"discount": 15,
"dose_id": 122975,
"pack_name": "10`S",
"pack_type": "STRIPS",
"pack": 10,
"pack_content_type": "TABLET",
"pack_info": "10 Tablet ( 10 / Strip )",
"images": [
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/11f0a11c5338fa78853c01c060f05aff5fe083ec1.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/ee2d2613347fad241b55ce73376ecf9554c31d7e1.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/2879aa3fec81e5bd749956007f13dc5756a761e51_cropped_not_compressed.jpg"
},
{
"res-750": "https://www.practostatic.com/practopedia-images/res-750/a5015b5b0bcd962f16431e6b08b86a165380ee002.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/21c1cb713e152160748854ad277b998a822f9cf02.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/cd1953d6084799a0f1304c7f4f69f58bb49f20e62_cropped_not_compressed.JPG"
},
{
"res-750": "https://www.practostatic.com/practopedia-images/res-750/1f9ca582b92f115cb5d1aa05bca92dd3d3f3073a3.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/714d7edfa4b7483653678ea897807de0062507dd3.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/77ffe7f6c3b069c77a7e15ecd3132c50fc0905b93_cropped_not_compressed.JPG"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/b1e5b1e81cf11d1711a1048b1ad3b137b8588c734.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/b1e5b1e81cf11d1711a1048b1ad3b137b8588c734.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/c02a6d970a0585929d9951459b8585616300eeb24_cropped_not_compressed.JPG"
},
{
"res-750": "https://www.practostatic.com/practopedia-images/res-750/1a6630090922dab35ca470546df5c0888bfd7dd75.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/1a6630090922dab35ca470546df5c0888bfd7dd75.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/8be062ba22ead8cfe85755618bbc0ca7ea1cb4075_cropped_not_compressed.JPG"
},
{
"res-750": "https://www.practostatic.com/practopedia-images/res-750/7b2a4dae4cc80d84fa341b12941d4d3e2d76688f6.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/7b2a4dae4cc80d84fa341b12941d4d3e2d76688f6.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/aa45ba2730f45b30f368dd03e4b29e9db7ae7b0b6_cropped_not_compressed.JPG"
}
]
}
},
{
"type": "drug",
"display_text": "Clocip Cream",
"mds_id": "01c9bd00-5d5b-43d3-8d35-317e5a1ea58f",
"drug": {
"regulatory_class_id": "1083d4e0-7591-4602-b230-82086f77f287",
"regulatory_class_name": "OTC",
"requires_prescription": False,
"productId": "def9f1fe-3060-4e3b-84ac-ef26958a315b",
"product_name": "CLOTRIMAZOLE (1 %) Cream",
"dosage_form_id": "8114226e-8765-4bcf-bc16-0aab82c3d543",
"dosage_form_name": "Cream",
"brand_id": "01c9bd00-5d5b-43d3-8d35-317e5a1ea58f",
"brand_name": "Clocip Cream",
"manufacturer_id": "6260f9b9-8d7f-4508-805e-5e3f1de3ea43",
"manufacturer_name": "Cipla Ltd.",
"slug": "clocip-1-cream-17208",
"pp_enabled": True,
"order_enabled": True,
"quantity_per_pack": 1,
"sub_type": "drug",
"type": "drug",
"indication_name": [
"Oral Thrush",
"Skin fungal infections",
"Vaginal Candidiasis"
],
"composition_name": "Clotrimazole",
"result_type": "fuzzy",
"is_available": False,
"mrp": 39.94,
"discount": 15,
"dose_id": 598552,
"pack_name": "1`S",
"pack_type": "UNIT",
"pack": 1,
"pack_content_type": "OINTMENT",
"pack_info": "1 Ointment",
"images": [
{
"res-750": "https://www.practostatic.com/practopedia-images/res-750/bc917d4ed28788f9d3c2f5012672c269cd33d9bc1.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/4ee793aabde269da8723518efcc5693782d98e071_cropped_not_compressed.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/6f5dd5b5345da563a55fb97df9ec481bba0991b41.JPG"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/0433a99038f63686db99d3c17339a150ec8fd6ce2_cropped_not_compressed.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/f698cbac673c35041e3706975fbfcf7b9b4e364f2.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/84045af1cda9ce74b6d2177fe2dde51195b2c90b2.JPG"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/54f343288046e14e285a8bd7087573e828d2591c3_cropped_not_compressed.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/dbadce2fc9e03c556e24a54ca685023cc74adebf3.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/dbadce2fc9e03c556e24a54ca685023cc74adebf3.JPG"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/b71fa9349faef143d925723945c0675234ab86d34_cropped_not_compressed.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/af2ea427c10bb79b89407db6395fc8bbf26174c94.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/e08570c7cbe6c11e3e60c5c34fcb12b58155b4374.JPG"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/452cacb83e45c34c047a2de19782e78de78122045_cropped_not_compressed.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/1dfe4649b086c40003f68d3c079d477f91261b4e5.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/ff52561c9452db54e8dd2a663c4d1e5d61bacbed5.JPG"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/5259495600b8d0017ec402081a998b857f3756626.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/c726fdd746a0f2075b313827dbfc37a835908df06.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/ae313753e99c662125c7b5320fb709c3a3dd8c486_cropped_not_compressed.JPG"
}
]
}
},
{
"type": "drug",
"display_text": "Crolim Ointment",
"mds_id": "366bae4b-0deb-4384-9d2a-4bd9166b8e95",
"drug": {
"regulatory_class_id": "4e0889e5-3859-4129-8fff-7a14a417ee38",
"regulatory_class_name": "Schedule G",
"requires_prescription": True,
"productId": "73f7050e-11ff-4f83-a4af-2dd67054a2ce",
"product_name": "Tacrolimus (0.1 %) Ointment",
"dosage_form_id": "f7bc6f40-d8e8-411b-8a2b-9fc2f2b7ee1f",
"dosage_form_name": "Ointment",
"brand_id": "366bae4b-0deb-4384-9d2a-4bd9166b8e95",
"brand_name": "Crolim Ointment",
"manufacturer_id": "5da5431b-a4fe-45c1-b601-29c899ee550d",
"manufacturer_name": "Sun Pharma Laboratories Ltd.",
"slug": None,
"pp_enabled": False,
"order_enabled": True,
"quantity_per_pack": 1,
"sub_type": "drug",
"type": "drug",
"result_type": "fuzzy",
"is_available": True,
"mrp": 629,
"discount": 15,
"dose_id": 123766,
"pack_name": "15GM",
"pack_type": "TUBE",
"pack": "15GM",
"pack_content_type": "OINTMENT",
"pack_info": "15gm Ointment"
}
},
{
"type": "drug",
"display_text": "Clocip Dusting Powder",
"mds_id": "71e7a5ec-6a37-4ccf-b601-b9508f79218c",
"drug": {
"regulatory_class_id": "1083d4e0-7591-4602-b230-82086f77f287",
"regulatory_class_name": "OTC",
"requires_prescription": False,
"productId": "1ff71f5f-f0b7-450b-bc77-bbd555d6e6a5",
"product_name": "CLOTRIMAZOLE (1 %) Dusting Powder",
"dosage_form_id": "7526bc01-98a0-4915-9fa3-3c0b933401fd",
"dosage_form_name": "Dusting Powder",
"brand_id": "71e7a5ec-6a37-4ccf-b601-b9508f79218c",
"brand_name": "Clocip Dusting Powder",
"manufacturer_id": "6260f9b9-8d7f-4508-805e-5e3f1de3ea43",
"manufacturer_name": "Cipla Ltd.",
"slug": "clocip-1-dusting-powder-17209",
"pp_enabled": True,
"order_enabled": True,
"quantity_per_pack": 1,
"sub_type": "drug",
"type": "drug",
"indication_name": [
"Oral Thrush",
"Skin fungal infections",
"Vaginal Candidiasis"
],
"composition_name": "Clotrimazole",
"result_type": "fuzzy",
"is_available": True,
"mrp": 61.5,
"discount": 15,
"dose_id": 121125,
"pack_name": "75GM",
"pack_type": "POWDER",
"pack": "75GM",
"pack_content_type": "DUSTING POWDER",
"pack_info": "75gm Dusting Powder",
"images": [
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/a7e291f5fff10a561d82b470be9ebe566c3f70291.jpg",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/a7e291f5fff10a561d82b470be9ebe566c3f70291.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/fbfc234d562794868b65efb77e2c8f5b11e574461_cropped_not_compressed.jpg"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/05edef14ae66d70ca228b26bf5d44b34d064c55d2_cropped_not_compressed.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/8fad2fb41e8aeee004f24f89ce09a20a71a464c62.jpg",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/8fad2fb41e8aeee004f24f89ce09a20a71a464c62.jpg"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/03efc6fa34990d5232e1f99cf8a22d98282d41d03.jpg",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/03efc6fa34990d5232e1f99cf8a22d98282d41d03.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/3f27d68de6d4a65d1621665c2ed6f5392f8ae35a3_cropped_not_compressed.jpg"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/5da94e447c92ee81ff2a6d8297f8ef11a06d776e4.jpg",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/5da94e447c92ee81ff2a6d8297f8ef11a06d776e4.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/ee9c3bc25fe45110fea569248a518523ab3733d34_cropped_not_compressed.jpg"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/a267f1f5c2cc1f3e836b3bc03d5bf1190df028d95_cropped_not_compressed.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/977d07cb986352d944ee3a74d8c8f83e5c7381f05.jpg",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/977d07cb986352d944ee3a74d8c8f83e5c7381f05.jpg"
}
]
}
},
{
"type": "drug",
"display_text": "Corcium Plus Capsule",
"mds_id": "1984b23e-934f-4124-9045-7f11a1a3849c",
"drug": {
"brand_id": "1984b23e-934f-4124-9045-7f11a1a3849c",
"brand_name": "Corcium Plus Capsule",
"product_name": None,
"regulatory_class_id": "8cbd390e-e850-4aab-abb9-f8f7925d21f0",
"regulatory_class_name": "Nutraceuticals",
"dosage_form_id": "0e9b14e9-d256-4209-be31-407ecd9a2bc6",
"dosage_form_name": "Capsule",
"requires_prescription": False,
"pp_enabled": False,
"sub_type": "general_product",
"type": "drug",
"order_enabled": True,
"quantity_per_pack": 10,
"manufacturer_id": "aa5ad259-19e7-4a5d-87ae-7699c3d74d35",
"manufacturer_name": "Lupin Ltd.",
"result_type": "fuzzy",
"is_available": True,
"mrp": 220,
"discount": 15,
"dose_id": 242550,
"pack_name": "10`S",
"pack_type": "STRIPS",
"pack": 10,
"pack_content_type": "CAPSULES",
"pack_info": "10 Capsules ( 10 / Strip )",
"images": [
{
"res-750": "https://www.practostatic.com/practopedia-images/res-750/c62316b36f6ccf33b94490951eaf84f2b249f96b1.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/48c00152b1f2ef8f58bc1c5fa686687b87bfe97b1_cropped_not_compressed.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/e8d49a37e98fad2abed918091faf26f8ffd096221.jpg"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/b9b56fdfafa54ce1827059b4a27f0e56f48b284e2.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/61d4c1a3a1f338c13d37d9cf66142d53f23150ec2_cropped_not_compressed.jpg",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/25fc4a30455d13ead5cac50ed5437341c798851d2.jpg"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/ae0d9c2a76c277a24642ad972a89e55c5caf51a33_cropped_not_compressed.jpg",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/c25821fa3c9a8a7baa594f0c3b81db7e4aba5fd43.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/c25821fa3c9a8a7baa594f0c3b81db7e4aba5fd43.jpg"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/12848e9340bc99daaaa0690f640e96f3914e4f6d4.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/e6bea98359fba87a870e14e1b486337a8a4e83aa4_cropped_not_compressed.jpg",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/ea34e88c4c05c3553de081e957b2bbf17d7f68994.jpg"
},
{
"res-750": "https://www.practostatic.com/practopedia-images/res-750/ea0c6267b0e92252609d53d83d7d24e936d50e935.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/243cb41fb0075428ea7bf4648f3383c90bedac8f5.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/9fce951f138c660b0f34cdda0d5bc54f1feb169e5_cropped_not_compressed.jpg"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/cbf2db0c2699bf1f3a7443f678b66a2ad7a816a16.jpg",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/de7ad140b0f874f56e273f66b686aa4d9827ee906.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/9474ddbc89293e22203c13fc711972689e1394276_cropped_not_compressed.jpg"
}
]
}
},
{
"type": "drug",
"display_text": "Corcium D3 Tablet",
"mds_id": "eb921028-5345-4126-ad93-1858b3256617",
"drug": {
"brand_id": "eb921028-5345-4126-ad93-1858b3256617",
"brand_name": "CORCIUM D3 TABLET",
"product_name": None,
"regulatory_class_id": "8cbd390e-e850-4aab-abb9-f8f7925d21f0",
"regulatory_class_name": "Nutraceuticals",
"dosage_form_id": "06513c41-2efe-4668-af90-84e410cae32b",
"dosage_form_name": "Tablet",
"requires_prescription": False,
"pp_enabled": False,
"sub_type": "general_product",
"type": "drug",
"order_enabled": True,
"quantity_per_pack": 15,
"manufacturer_id": "aa5ad259-19e7-4a5d-87ae-7699c3d74d35",
"manufacturer_name": "Lupin Ltd.",
"result_type": "fuzzy",
"is_available": True,
"mrp": 198,
"discount": 15,
"dose_id": 620637,
"pack_name": "15`S",
"pack_type": "STRIPS",
"pack": 15,
"pack_content_type": "TABLET",
"pack_info": "15 Tablet ( 15 / Strip )"
}
},
{
"type": "drug",
"display_text": "Clocip B Cream",
"mds_id": "1e9f800d-f0b1-42e9-8e36-44582685430a",
"drug": {
"regulatory_class_id": "1083d4e0-7591-4602-b230-82086f77f287",
"regulatory_class_name": "OTC",
"requires_prescription": False,
"productId": "27ef67e1-9389-4dc8-82fd-17109228be5a",
"product_name": "CLOTRIMAZOLE + BECLOMETASONE  (1/0.025 %) Cream",
"dosage_form_id": "8114226e-8765-4bcf-bc16-0aab82c3d543",
"dosage_form_name": "Cream",
"brand_id": "1e9f800d-f0b1-42e9-8e36-44582685430a",
"brand_name": "Clocip B Cream",
"manufacturer_id": "6260f9b9-8d7f-4508-805e-5e3f1de3ea43",
"manufacturer_name": "Cipla Ltd.",
"slug": None,
"pp_enabled": False,
"order_enabled": True,
"quantity_per_pack": 1,
"sub_type": "drug",
"type": "drug",
"result_type": "fuzzy",
"is_available": True,
"mrp": 40,
"discount": 15,
"dose_id": 121129,
"pack_name": "10GM",
"pack_type": "TUBE",
"pack": "10GM",
"pack_content_type": "CREAM",
"pack_info": "10gm Cream",
"images": [
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/38717d75670bb95bb38ce26211e15bf6458e804c1_cropped_not_compressed.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/6b52b12cea4c318d119bd1a3508dba08a4c5c19a1.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/b4f470c4eb14f12c2aa55b7d52210a077044a6fd1.JPG"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/5f1ed201c4ffce71c490df9ded41e398f816c0fd2_cropped_not_compressed.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/cfc835d21e1d9b106396a536aeab5f36cb58dc602.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/cfc835d21e1d9b106396a536aeab5f36cb58dc602.JPG"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/727febbe105e9c59a7b2acfc7004fa0792b08c8d3.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/6d2469526d09de5bafc5713f54a769c7fe92bcaa3_cropped_not_compressed.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/424c79fc1dd96bc525e733dd6ae94456caa0e1393.JPG"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/0e77bedc2017e4c518a869a8ac03c9d58f630e8b4.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/0e77bedc2017e4c518a869a8ac03c9d58f630e8b4.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/961928f30160a41590f1846b2482d4baa4c8249f4_cropped_not_compressed.JPG"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/22fb689a06672b888adf5322bbdac7cbf6a63da25_cropped_not_compressed.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/6cc88ee01e5d3212bdc8cc2b74523d8852a2a27c5.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/e114cd06fbdfb87493c1df55cde84f444c1bdb575.JPG"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/0174594ac21c6f67b941523d99a536c54bcf72f26.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/0174594ac21c6f67b941523d99a536c54bcf72f26.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/f787e8832f00876f3be1e1368bb331a72e687f2c6_cropped_not_compressed.JPG"
}
]
}
},
{
"type": "drug",
"display_text": "Clocip B Cream",
"mds_id": "1e9f800d-f0b1-42e9-8e36-44582685430a",
"drug": {
"regulatory_class_id": "1083d4e0-7591-4602-b230-82086f77f287",
"regulatory_class_name": "OTC",
"requires_prescription": False,
"productId": "27ef67e1-9389-4dc8-82fd-17109228be5a",
"product_name": "CLOTRIMAZOLE + BECLOMETASONE  (1/0.025 %) Cream",
"dosage_form_id": "8114226e-8765-4bcf-bc16-0aab82c3d543",
"dosage_form_name": "Cream",
"brand_id": "1e9f800d-f0b1-42e9-8e36-44582685430a",
"brand_name": "Clocip B Cream",
"manufacturer_id": "6260f9b9-8d7f-4508-805e-5e3f1de3ea43",
"manufacturer_name": "Cipla Ltd.",
"slug": None,
"pp_enabled": False,
"order_enabled": True,
"quantity_per_pack": 1,
"sub_type": "drug",
"type": "drug",
"result_type": "fuzzy",
"is_available": True,
"mrp": 24,
"discount": 15,
"dose_id": 597053,
"pack_name": "5GM",
"pack_type": "TUBE",
"pack": "5GM",
"pack_content_type": "CREAM",
"pack_info": "5gm Cream",
"images": [
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/72a674f9022b6c8e95e312cedc6103cf481eb8f81_cropped_not_compressed.jpg",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/3ef6c28765a13cf32bb5d00235118f225d9076ff1.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/095e34f4a051e1d9ae22363c265067c07b3e1fd21.jpg"
},
{
"res-750": "https://www.practostatic.com/practopedia-images/res-750/37225cae73010726a46cbbe73d76c1dee565689d2.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/37225cae73010726a46cbbe73d76c1dee565689d2.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/f5a06ba538bb8584538e09c53f14b259a1d01c7c2_cropped_not_compressed.jpg"
},
{
"res-750": "https://www.practostatic.com/practopedia-images/res-750/63ee61b06effc25a6bdcf8692347cde7aba4f9533.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/c76f35087ecd923096c368ec13151dbbb993a35a3_cropped_not_compressed.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/63ee61b06effc25a6bdcf8692347cde7aba4f9533.jpg"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/f441df42bd05940cebbd8d2022895937e8d245654_cropped_not_compressed.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/a8a64d2870f6acd0072eae21de9923162e9b97d34.jpg",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/6ae19057f4e498e372867653143435fe63836aa64.jpg"
},
{
"res-750": "https://www.practostatic.com/practopedia-images/res-750/6fa5e1734654795a2048056236ce8d74cc6cb92f5.jpg",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/cb20d4704eba69d19e6d7284623fb3f49bedd0ca5.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/ff9e7d4b6eb80dad1ee5719ca4da141d8e2c2c945_cropped_not_compressed.jpg"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/173b89c73c26387f9eae498538c82c1a461e47fe6.jpg",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/173b89c73c26387f9eae498538c82c1a461e47fe6.jpg",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/5f93546fd24ffd02316181d67a757c23073149fa6_cropped_not_compressed.jpg"
}
]
}
},
{
"type": "drug",
"display_text": "Corcium K2 Tablet",
"mds_id": "ddc78534-282b-47d5-8f2e-1a60c5d07a29",
"drug": {
"brand_id": "ddc78534-282b-47d5-8f2e-1a60c5d07a29",
"brand_name": "Corcium K2 Tablet",
"product_name": None,
"regulatory_class_id": "8cbd390e-e850-4aab-abb9-f8f7925d21f0",
"regulatory_class_name": "Nutraceuticals",
"dosage_form_id": "06513c41-2efe-4668-af90-84e410cae32b",
"dosage_form_name": "Tablet",
"requires_prescription": False,
"pp_enabled": False,
"sub_type": "general_product",
"type": "drug",
"order_enabled": True,
"quantity_per_pack": 10,
"manufacturer_id": "aa5ad259-19e7-4a5d-87ae-7699c3d74d35",
"manufacturer_name": "Lupin Ltd.",
"result_type": "fuzzy",
"is_available": True,
"mrp": 196,
"discount": 15,
"dose_id": 122976,
"pack_name": "10`S",
"pack_type": "STRIPS",
"pack": 10,
"pack_content_type": "TABLET",
"pack_info": "10 Tablet ( 10 / Strip )",
"images": [
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/2d2b1705403b0a221f4bb12ffb3cb598fc37f4a41.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/4ee05a5552a3a9b4afb80ad5d82c9ea573cb809e1.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/268ff1d210b29442121c95aca8565026777983221_cropped_not_compressed.jpg"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/00ed66ed5d89b2a9a837098b22ea8768f7b3fb4c2.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/ced5321108579c3ee84b1e284aa0850831beac7f2_cropped_not_compressed.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/00ed66ed5d89b2a9a837098b22ea8768f7b3fb4c2.JPG"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/8179f02e6267599af8860ccd2dbd7fd3649cae543_cropped_not_compressed.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/54bc261b7a1bc4392fd1437b834f320f4af5c6993.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/1908df5348c89373bd9df9321c5b45b0abe62eb13.JPG"
},
{
"res-master": "https://www.practostatic.com/practopedia-images/res-master/e41fd89c53c9d6af32bd193f7fb01cf8e096791f4_cropped_not_compressed.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/29e45dcaac39cb1ce659a7c3d32a93d9c55cd3574.JPG",
"res-150": "https://www.practostatic.com/practopedia-images/res-150/607f67c4410b96a4093a6452da0e0c309868535b4.JPG"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/6dd73777990f5e32457a394b880546a2e29826b55.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/6dd73777990f5e32457a394b880546a2e29826b55.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/69bb0b58bbf76d27c629c717a9d387490d437bd45_cropped_not_compressed.JPG"
},
{
"res-150": "https://www.practostatic.com/practopedia-images/res-150/e1a3d6815838cbeadccb33bf6ee43c7e36f5ed106.JPG",
"res-750": "https://www.practostatic.com/practopedia-images/res-750/25da975068ed2b48419c1d43529169ea0bc0a57a6.JPG",
"res-master": "https://www.practostatic.com/practopedia-images/res-master/bb6173f020d868a6a4aba1dd564b288849f174ce6_cropped_not_compressed.JPG"
}
]
}
},
{
"type": "drug",
"display_text": "Cocid D Capsule",
"mds_id": "f2a29e93-22bc-410e-992d-81dfb63c565a",
"drug": {
"regulatory_class_id": "2ef5c706-df02-4eea-83bc-e22e9b332cfc",
"regulatory_class_name": "Schedule H",
"requires_prescription": True,
"productId": "b2d90351-e6ea-4f90-af5d-971b26fe8f93",
"product_name": "Pantoprazole (20 mg) + Domperidone (10 mg) Capsule",
"dosage_form_id": "b69d9a2c-174a-4e95-b21f-49456c1326f7",
"dosage_form_name": "Capsule",
"brand_id": "f2a29e93-22bc-410e-992d-81dfb63c565a",
"brand_name": "Cocid D Capsule",
"manufacturer_id": "0db3a03a-64c7-4939-a639-b0039002e08f",
"manufacturer_name": "Talent India",
"slug": "cocid-d-capsule-48728",
"pp_enabled": True,
"order_enabled": True,
"quantity_per_pack": 10,
"sub_type": "drug",
"type": "drug",
"indication_name": [
"Gastroesophagal Reflux Disease"
],
"composition_name": "Domperidone (10 mg) + Pantoprazole (20 mg)",
"result_type": "fuzzy",
"is_available": True,
"mrp": 77.5,
"discount": 15,
"dose_id": 486159,
"pack_name": "10`S",
"pack_type": "STRIPS",
"pack": 10,
"pack_content_type": "CAPSULES",
"pack_info": "10 Capsules ( 10 / Strip )"
}
}
];

app = Flask(__name__)
@app.route('/', methods = ['GET'])
def home():
	return render_template('login.html')

@app.route("/login", methods = ['POST'])
def index():
	if request.method == "POST":
		email = request.form['email']
		pswd = request.form['pswd']
		name="null"
		if(email == "vishal@gmail.com" and pswd == "12345"):
			name="Vishal"
		return render_template('homepage.html', name = name)


@app.route("/getmedicines",methods=['GET'])
def getJson():
	return jsonify(medicine_json)

@app.route("/getDrugData",methods=['GET'])
def getMedicinePage():
	id = request.args.get('id')
	return render_template('medicinePage.html',id=id)

if __name__ == "__main__":
	app.debug=True
	app.run(host="0.0.0.0",port=8080)