using UnityEngine;
using System.Collections;

public class PlayerBehaviour : MonoBehaviour {
	public float Health = 100.0f;
	public float Speed = 10.0f;
	// Movement control vars
	private Vector3 _pointA;
	public Vector3 PointB;
	// Use this for initialization
	void Start () {
		_pointA = this.transform.position;
	}
	// Update is called once per frame
	void Update () {
		this.transform.position = Vector3.Lerp(_pointA, PointB, Mathf.Cos(Time.time * Speed));
	}
}
