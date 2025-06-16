<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class OrderDetail extends Model
{
    use HasFactory;
    protected $fillable = [
        'order_id',
        'product_id',
        'price',
        'quantity'
    ];
    protected $casts = [
        'price' => 'integer' 
    ];
    public function order(){
        return $this->belongsTo(Order::class, 'order_id', 'id');
    }
    public function product(){
        return $this->belongsTo(Product::class, 'product_id', 'id');
    }
    public function getTotalAttribute()
    {
        return $this->price * $this->quantity;
    }
}
