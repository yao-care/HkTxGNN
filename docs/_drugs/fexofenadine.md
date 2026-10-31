---
layout: default
title: Fexofenadine
parent: 僅模型預測 (L5)
nav_order: 375
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
monitor_inn: "Fexofenadine"
predicted_indications: ["rosacea conjunctivitis"]
description: "Fexofenadine：預測新適應症為酒糟性結膜炎 (rosacea conjunctivitis)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Fexofenadine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Fexofenadine: 酒糟性結膜炎 (rosacea conjunctivitis)
{: .text-alpha }

## 一句話總結

Fexofenadine 是第二代選擇性周邊 H1 組織胺受體拮抗劑，原本用於過敏性鼻炎、異位性結膜炎、特發性蕁麻疹等過敏相關疾病。
TxGNN 模型預測它可能對**酒糟性結膜炎 (Rosacea Conjunctivitis)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 酒糟性結膜炎 (rosacea conjunctivitis) |
| TxGNN 預測分數 | 0.9985 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Fexofenadine 屬於選擇性周邊 H1 受體拮抗劑，已用於過敏性與異位性結膜炎，機轉上可能透過阻斷組織胺引起的眼表發炎、搔癢與血管擴張，而適用於結膜炎類疾病。以上機轉說明屬一般藥理知識，並未由本次彙整的資料驗證。

不過，酒糟性（眼型酒糟）結膜炎的成因主要是瞼板腺功能障礙、淚膜不穩定、蠕形蟎或微生物定植，以及先天免疫與神經血管失調，組織胺的角色有限。此外，口服 Fexofenadine 到達眼表的濃度有限，H1 阻斷以外的抗發炎作用（例如減少肥大細胞介質釋放）在此疾病中尚未證實。

0.9985 的高分來自 TxGNN 模型（深度學習），可能反映模型在相關疾病之間學到的相似性，並非生物學證據，也不代表有針對酒糟性結膜炎的實證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 20 張有效的單一成分許可證，皆為錠劑，目前資料未載明劑型與核准適應症文字。以下列出 5 張主要許可證：

| 許可證號 | 品名 | 廠商 | 規格 |
|---------|------|------|------|
| HK-56373 | BOSNUM TAB | Health Alliance International Co Ltd | 60 mg |
| HK-61666 | BOSNUM 180 TABLETS | Health Alliance International Co Ltd | 180 mg |
| HK-67128 | ALEACT 180 TABLETS | R. Manstien (Australia) Limited | 180 mg |
| HK-68487 | NAXODINE TABLETS | Welldone Pharmaceuticals Limited | 180 mg |
| HK-55609 | AXODIN 120 TAB | Eugenpharm International Limited | 120 mg |

## 安全性考量

- **知識圖譜標示的相關禁忌疾病**（來自藥物與疾病關聯資料，非仿單原文，需以仿單核實）：高血壓、腎臟疾病、糖尿病與糖尿病酮酸中毒、良性前列腺增生、冠狀動脈疾病與動脈硬化、閉鎖角青光眼、甲狀腺功能亢進（含葛瑞夫茲氏病）。
- **藥物交互作用**：資料庫共收錄 100 筆，以下為部分範例：
  - 中度：Eliglustat、Eluxadoline、Rolapitant，以及含鎂或鋁的制酸劑（氫氧化鎂、氫氧化鋁、Magaldrate、碳酸鎂）
  - 輕度：Clarithromycin、Miconazole、Clotrimazole

仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有模型預測（L5），沒有臨床試驗或文獻佐證。
- 酒糟性結膜炎的主要病理並非組織胺驅動，加上口服藥物的眼表濃度有限，機轉上的合理性偏弱。
- 仿單安全性資料尚缺，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌資料，完成安全性篩選
- 補齊作用機轉資料（DrugBank）
- 系統性檢索酒糟性結膜炎與抗組織胺的臨床及前臨床研究
- 評估給藥途徑（口服對比眼用劑型）是否能達到眼表有效濃度
- 釐清酒糟性結膜炎中組織胺或肥大細胞參與的證據，再決定是否啟動探索性研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

