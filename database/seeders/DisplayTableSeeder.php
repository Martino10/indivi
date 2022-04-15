<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use DB;

class DisplayTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        DB::table('display')->insert([
            'digits' => '404'
        ]);
    }
}
