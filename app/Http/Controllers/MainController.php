<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Display;

class MainController extends Controller
{
    public function show() {
        $display = Display::all()->first();
        return view('main')->with('display', $display);
    }
}
