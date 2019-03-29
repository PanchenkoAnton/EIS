db.collection.aggregate([
{$unwind: "$sessions" },
{$unwind: "$sessions.actions"},
{$group: {_id: {number: "$number", type: "$sessions.actions.type"}, last: {$max: "$sessions.actions.created_at"}, count: {$sum: 1}}},
{$addFields: { type: "$_id.type", number: "$_id.number" }},
{$project: { _id: 0, type: 1, last: 1, count: 1, number: 1}}
]).pretty()
