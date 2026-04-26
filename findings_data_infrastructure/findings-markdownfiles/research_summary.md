# Data Infrastructure Research Summary

## Key Topics to Cover
1. Data Lakes vs Warehouses vs Lakehouses - lakehouse is the modern default, Delta Lake/Iceberg
2. Feature Stores - Feast (OSS), Tecton (managed), training-serving skew, point-in-time joins
3. Data Versioning - DVC (pointer files in git, data in remote storage), lakeFS
4. Labeling - Labelbox, Scale AI, active learning for labeling, weak supervision (Snorkel)
5. Data Pipelines - Airflow (legacy standard), Prefect (pythonic), Dagster (asset-centric)
6. Streaming Data - Kafka (message broker), Flink (stream processing), windowing
7. Data Validation - Great Expectations (vendor-neutral), TFDV (TF ecosystem)
8. Data Catalogs - DataHub, OpenMetadata, Amundsen
9. Privacy - Differential privacy (epsilon budget, noise), Federated learning (model updates not data)

## Running Example Idea
- A food delivery startup "BiteBridge" building a recommendation system
- Starts tiny: 3 restaurants, 5 users, grows organically
- Threads through every section naturally

## Concept Ladder
1. Where does data live? (storage) → warehouse vs lake → limitation → lakehouse
2. How does data move? (pipelines) → batch → limitation → streaming → Kafka/Flink
3. Who orchestrates? → cron → limitation → Airflow/Prefect/Dagster
4. How do we serve features? → manual → training-serving skew → feature stores
5. How do we version data? → "just copy it" → limitation → DVC
6. How do we get labels? → manual → limitation → active learning → weak supervision
7. How do we trust data? → silent corruption → data validation
8. How do we find data? → "ask Dave" → data catalogs
9. How do we protect data? → privacy → differential privacy + federated learning

## Vulnerability Moments
- Confession: avoided data infrastructure, thought models were everything
- Training-serving skew story: spent weeks debugging model, was a feature definition mismatch
- Still uncertain about when streaming is truly needed vs overengineered
- Oversimplification: initially said "warehouse = structured, lake = unstructured" but truth is muddier
- Differential privacy epsilon - still developing intuition for right values

## Analogies
- Kitchen analogy: pantry (lake), recipe book shelf (warehouse), modern kitchen with both (lakehouse)
- Water utility: pipes (pipelines), reservoir (storage), water treatment (validation), meter (monitoring)
