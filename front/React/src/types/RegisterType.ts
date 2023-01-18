// バックエンドからのレスポンスの型定義
export type User = {
  id: number;
  user_id: number;
  user_name: string;
  // joined_date: Date;
  access_token: string;
};
