// package HASHING;

import java.util.HashMap;

public class hashmapdemo {
    public static void main(String[] args) {
        HashMap<String, Integer> map = new HashMap<>();
        map.put("venky", 2005);
        System.out.println(map);
        map.put("saiKumar", 2004);
        String name = "venky";
        System.out.println(name.hashCode());
        if (name.hashCode() == 112093517) {
            System.out.println("True");
        }
        /*
         * map.clear();//Remove the all Keys and Values
         * System.out.println(code instanceof String);//typeof(x) in JavaScript
         */
        System.out.println(map.size());
        // map.remove("venky");
        System.out.println(map.getOrDefault("venky", 89));
        System.out.println(map.containsKey("venky"));
        System.out.println(map.get("venky"));
        Hashdemo set = new Hashdemo();// set object is created to add entities
        set.put("Apple", "venky");
        set.put("Watermelon", "nagesh");
        set.put("Grape", "chaitu");
        set.put("Papaya", "sai");
        System.out.println(set.get("Apple"));
        set.remove("watermelon");// This won't work because it contains

        System.out.println(set.get("Watermelon"));
        System.out.println(set.get("Papaya"));
        System.out.println(set.get("Grape"));

    }

    public static class Hashdemo {
        private Entity[] entities;

        public Hashdemo() {// Constructor for Hashdemo
            entities = new Entity[100];
        }

        public void put(String key, String value) {// set method
            int hash = Math.abs(key.hashCode() % entities.length);
            entities[hash] = new Entity(key, value);
        }

        public String get(String key) {// get method
            int hash = Math.abs(key.hashCode() % entities.length);
            if (entities[hash] != null && entities[hash].key.equals(key)) {
                return entities[hash].value;
            } else
                return null;
        }

        public String remove(String key) {// remove method
            int hash = Math.abs(key.hashCode() % entities.length);
            if (entities[hash] != null && entities[hash].key.equals(key)) {
                return entities[hash].value = null;
            } else
                return null;

        }

        private class Entity {// Entity class
            String key;
            String value;

            public Entity(String key, String value) {
                this.key = key;
                this.value = value;
            }
        }

    }
}
