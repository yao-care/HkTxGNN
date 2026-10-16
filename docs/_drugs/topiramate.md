---
layout: default
title: Topiramate
parent: 僅模型預測 (L5)
nav_order: 890
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Topiramate：預測新適應症為三叉神經腫瘤 (Trigeminal Nerve Neoplasm)（證據等級 L5）。原適應症：癲癇（全身性強直陣攣發作、局部癲癇、Lennox-Gastaut 症候群等）"
monitor_inn: "TOPIRAMATE"
predicted_indications: ["trigeminal nerve neoplasm", "visual epilepsy", "micturation-induced seizures", "audiogenic seizures", "startle epilepsy"]
---

# Topiramate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Topiramate：從癲癇到三叉神經腫瘤

## 一句話總結

Topiramate 是一種抗癲癇藥物，原本用於全身性強直陣攣發作、局部癲癇及 Lennox-Gastaut 症候群等癲癇相關適應症。
TxGNN 模型預測分數最高的新適應症是**三叉神經腫瘤 (Trigeminal Nerve Neoplasm)**，但目前**沒有任何臨床試驗或文獻**支持這項預測，僅屬模型推論。
同一批預測中，證據相對較多的是反射性癲癇類（如聽源性癲癇發作），但這些較接近原適應症的延伸，而非真正的新用途。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 癲癇（全身性強直陣攣發作、局部癲癇、Lennox-Gastaut 症候群等） |
| 預測新適應症 | 三叉神經腫瘤 (Trigeminal Nerve Neoplasm) |
| TxGNN 預測分數 | 99.70% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

註：原適應症來自知識圖譜的適應症資料，香港許可證本身未載明核准適應症文字。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般已知 topiramate 是抗癲癇藥物，其作用涉及鈉離子通道阻斷、增強 GABA-A 活性、拮抗 AMPA/kainate 受體，以及微弱的碳酸酐酶抑制。這些作用與癲癇的神經興奮性有關。

這些機轉與三叉神經腫瘤的腫瘤生物學之間，目前沒有已知的明確關聯。模型給出高分，較可能是因為知識圖譜中該疾病與神經痛或癲癇節點相近，而非 topiramate 具有抗腫瘤活性。因此這項預測的機轉合理性偏低，應視為待驗證的假說。

### 其他預測適應症概覽

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|-----------|-----------|---------|------|
| 1 | 三叉神經腫瘤 | 99.70% | L5 | Hold |
| 2 | 視覺性癲癇 (Visual Epilepsy) | 99.28% | L4 | Research Question |
| 3 | 排尿誘發性癲癇發作 | 99.21% | L4 | Research Question |
| 4 | 聽源性癲癇發作 (Audiogenic Seizures) | 99.21% | L4 | Research Question |
| 5 | 驚嚇性癲癇 (Startle Epilepsy) | 99.21% | L5 | Hold |

其中視覺性、排尿誘發性、聽源性與驚嚇性癲癇都屬反射性癲癇，與 topiramate 現有的癲癇適應症高度重疊，較像現有適應症的延伸。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

（針對排名第 1 的三叉神經腫瘤，未找到任何文獻。）

---

## 香港上市資訊

香港共有 20 張有效許可證，均為單一成分製劑，無已取消者。以下列出 5 張主要許可證（資料中未載明劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-42315 | TOPAMAX TAB 25MG（Johnson & Johnson） | 錠劑 | 未載明 |
| HK-42316 | TOPAMAX TAB 50MG（Johnson & Johnson） | 錠劑 | 未載明 |
| HK-42317 | TOPAMAX TAB 100MG（Johnson & Johnson） | 錠劑 | 未載明 |
| HK-63959 | TOPIRAMATE SANDOZ TABLET 50MG（Sandoz） | 錠劑 | 未載明 |
| HK-55963 | APO-TOPIRAMATE TAB 25MG（Hind Wing） | 錠劑 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（來自知識圖譜關聯，並非仿單文字）：焦慮症、神經症、輕度憂鬱症、腎臟疾病、輸尿管膿腫、肝臟疾病、膽囊疾病、腹瀉性疾病、高眼壓、腎結石（含 SLC26A1 相關易感性）、急性尿酸腎病變、酸中毒、代謝性酸中毒、失憶症、逆行性失憶。
- **藥物交互作用**：共查得 100 筆，以下為主要項目：
  - **嚴重 (Major)**：Metformin、Hyoscyamine、Atropine、Scopolamine、Glycopyrronium、Clidinium、Dicyclomine、Mepenzolate、Methscopolamine、Propantheline、Trospium（多為抗膽鹼藥物）
  - **中度 (Moderate)**：Pioglitazone、Morphine、Dronabinol、Phentermine、Metoclopramide、Nabilone、Glyburide、Phenylbutyric acid、Glycerol phenylbutyrate

仿單的主要警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第 1 的三叉神經腫瘤預測分數雖高，但沒有臨床試驗與文獻，topiramate 的機轉與腫瘤生物學也無已知關聯，目前僅屬模型推論（L5）。
- 證據較多的反射性癲癇（尤其聽源性癲癇發作有 topiramate 動物模型研究）屬現有癲癇適應症的延伸，且仍缺乏人體臨床證據。

**若要推進需要：**
- 補齊 topiramate 的作用機轉資料（MOA）
- 針對三叉神經腫瘤進行文獻與前臨床檢索，確認是否存在抗腫瘤或神經痛相關訊號
- 取得香港衛生署仿單的警語與禁忌症，完成安全性篩選
- 若轉向反射性癲癇，蒐集病例報告或小型臨床研究，作為人體證據
- 評估 topiramate 在腫瘤病人使用時的風險，特別是腎結石、代謝性酸中毒與認知影響
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

