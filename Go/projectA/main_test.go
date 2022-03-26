package main

import "testing"

func Test_isPrime(t *testing.T) {
	type args struct {
		num int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
		{
			name: "base case 1",
			args: args{
				num: 2,
			},
			want: true,
		},
		{
			name: "base case 2",
			args: args{
				num: 1,
			},
			want: false,
		},
		{
			name: "base case 3",
			args: args{
				num: 0,
			},
			want: false,
		},
		{
			name: "Test 1",
			args: args{
				num: 29,
			},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isPrime(tt.args.num); got != tt.want {
				t.Errorf("isPrime() = %v, want %v", got, tt.want)
			}
		})
	}
}
