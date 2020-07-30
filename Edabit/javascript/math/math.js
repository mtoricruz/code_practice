// 1
function hurdleJump(hurdles, jumpHeight) {
	return Math.max(...hurdles) <= jumpHeight
}
// Logical operator (ex: <=, <, >, ==) returns a True if correct and False if not