from datetime import datetime, timezone

from bson import ObjectId

from app.database.mongodb import analyses_collection


def save_analysis(data: dict) -> str:
    """Save an analysis result to MongoDB."""

    document = {
        **data,
        "created_at": datetime.now(timezone.utc),
    }

    result = analyses_collection.insert_one(document)

    return str(result.inserted_id)


def get_analysis(analysis_id: str):
    """Get a single analysis by its MongoDB ID."""

    if not ObjectId.is_valid(analysis_id):
        return None

    return analyses_collection.find_one({"_id": ObjectId(analysis_id)})


def get_recent_analyses(limit: int = 20):
    """Get the most recent analyses."""

    return list(analyses_collection.find().sort("created_at", -1).limit(limit))
