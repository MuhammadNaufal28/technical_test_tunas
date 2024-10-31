CREATE TABLE "tunas_room"(
    "id" BIGINT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "type_room" CHAR(255) NOT NULL,
    "location_room" CHAR(255) NOT NULL,
    "capacity" VARCHAR(255) NOT NULL,
    "notes" TEXT NOT NULL
);
ALTER TABLE
    "tunas_room" ADD PRIMARY KEY("id");
CREATE TABLE "tunas_booking_room"(
    "id" BIGINT NOT NULL,
    "no" VARCHAR(255) NOT NULL,
    "tunas_room_id" VARCHAR(255) NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "date" DATE NOT NULL
);
ALTER TABLE
    "tunas_booking_room" ADD PRIMARY KEY("id");
ALTER TABLE
    "tunas_room" ADD CONSTRAINT "tunas_room_name_foreign" FOREIGN KEY("name") REFERENCES "tunas_booking_room"("tunas_room_id");