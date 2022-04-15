<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use \App\Models\Display;

class DisplayController extends Controller
{
    public function show(Request $request) {
        $newDigits = $request->digits;
        if ($newDigits != "") {
            Display::where('id',1)->update(['digits'=> $newDigits]);
        }
        
        return redirect('/');
    }
}
