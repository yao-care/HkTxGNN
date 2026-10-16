---
layout: default
title: Avatrombopag
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Avatrombopag：預測新適應症為巨型血小板低下合併二尖瓣閉鎖不全 (marcothrombocytopenia with mitral valve insufficien…（證據等級 L5）。原適應症：血小板低下症（Thrombocytopenia）"
---

# Avatrombopag
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Avatrombopag：從血小板低下症到「巨型血小板低下合併二尖瓣閉鎖不全」

## 一句話總結

Avatrombopag 是口服血小板生成素受體（TPO 受體）促效劑，原本用於治療血小板低下症（thrombocytopenia）。
TxGNN 模型預測它可能對**巨型血小板低下合併二尖瓣閉鎖不全 (marcothrombocytopenia with mitral valve insufficiency)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 血小板低下症（Thrombocytopenia） |
| 預測新適應症 | 巨型血小板低下合併二尖瓣閉鎖不全 (marcothrombocytopenia with mitral valve insufficiency) |
| TxGNN 預測分數 | 99.995% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Avatrombopag 是口服 TPO 受體（c-Mpl）促效劑，能刺激巨核細胞增生與分化，進而提高血小板數量。目前缺乏 DrugBank 的詳細作用機轉資料，以上說明來自本報告整理的機轉推論。

就「血小板低下」這個成分而言，機轉上有合理的關聯。但這個疾病的巨型血小板低下較可能源自先天性的血小板生成或結構缺陷（例如細胞骨架或 filamin 相關異常），因此藥物是否有效並不確定。至於二尖瓣閉鎖不全，與此藥物沒有任何機轉上的關聯。

TxGNN 分數很高，但這只是計算預測，沒有試驗或文獻佐證。

**其他排名較前的預測（皆為 L5、建議 Hold）：**

| 排名 | 預測適應症 | 分數 | 簡評 |
|------|-----------|------|------|
| 2 | 血小板正常的遺傳性血小板低下症 | 99.995% | 機轉上可行，但疾病定義模糊、病因不明；其他 TPO 促效劑在遺傳性血小板低下症僅有有限且依亞型而異的資料 |
| 3 | 暫時性新生兒血小板低下症 | 99.995% | 疾病可自行緩解，用藥效益風險比不佳；無新生兒安全性資料 |
| 4 | 緻密顆粒病 (dense granule disease) | 99.995% | 問題在血小板功能而非數量；TPO 促效劑有血栓風險疑慮 |
| 5–10 | 肌萎縮性脊髓側索硬化症 (ALS) 及其感受性條目、下運動神經元症候群、Mills 症候群、單肢肌萎縮症、雙側旁矢狀頂枕多小腦回症 | 99.99%–99.993% | 與 TPO 路徑無明確機轉關聯，高分可能來自知識圖譜的網路結構假象 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68734 | DOPTELET TABLETS 20MG | 未提供 | 未提供 |

製造商為 FOSUN INDUSTRIAL CO., LIMITED，屬單一成分製劑，狀態有效。

---

## 安全性考量

- **藥物交互作用**：已查詢到 52 筆交互作用，以下列出部分主要項目：
  - **嚴重 (Major)**：Fosphenytoin、Carbamazepine、Carfilzomib、Dabrafenib、Enzalutamide、Fluconazole、Imatinib
  - **中度 (Moderate)**：Clarithromycin、Nitisinone、Cobicistat、Fosamprenavir、Gemfibrozil、Fenofibrate、Apalutamide、Atazanavir 等
- **其他提醒**：TPO 促效劑類藥物有增加血栓風險的疑慮（尤其在緻密顆粒病等情境下需留意）；用於新生兒或兒童的安全性資料尚未建立。

其餘警語與禁忌症資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有 TxGNN 模型分數，沒有臨床試驗或文獻支持（L5）。排名第一的預測只有血小板低下部分具機轉合理性，另一部分（二尖瓣閉鎖不全）並無關聯，且病因可能是先天結構缺陷。
- 香港許可證資料缺少核准適應症文字，且仿單警語與禁忌症資料尚未取得，無法進行安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，確認警語、禁忌症與核准適應症
- 補充詳細的作用機轉資料（如 DrugBank）
- 釐清「巨型血小板低下合併二尖瓣閉鎖不全」的病因與基因亞型，評估 TPO 促效劑是否適用
- 搜尋 TPO 促效劑（如 eltrombopag、romiplostim）在遺傳性血小板低下症的證據，作為間接佐證
- 若考慮較有機轉基礎的預測（如遺傳性血小板低下症），先設計小規模探索性研究或病例系列，並建立血栓風險監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

