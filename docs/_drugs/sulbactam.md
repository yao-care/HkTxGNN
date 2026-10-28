---
layout: default
title: Sulbactam
parent: 僅模型預測 (L5)
nav_order: 837
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "SULBACTAM"
predicted_indications: ["bacterial arthritis"]
description: "Sulbactam：預測新適應症為細菌性關節炎 (bacterial arthritis)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Sulbactam
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

## Sulbactam: 細菌性關節炎 (bacterial arthritis)
{: .text-alpha }

## 一句話總結

Sulbactam 是一種不可逆的 β-內醯胺酶抑制劑，原本用於膽管炎、金黃色葡萄球菌感染及大腸桿菌感染等細菌性疾病。
TxGNN 模型預測它可能對**細菌性關節炎 (Bacterial Arthritis)** 有效，
目前**沒有臨床試驗登記**，但有 **20 篇相關文獻**，其中數篇為 sulbactam/ampicillin 用於骨關節感染的臨床研究。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 細菌性關節炎 (bacterial arthritis) |
| TxGNN 預測分數 | 0.9979 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 8 張／共 8 張） |
| 許可證數 | 8 張（有效 8 張） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏經整理的詳細作用機轉資料。根據藥物類別推論，Sulbactam 是不可逆的 β-內醯胺酶抑制劑，本身也能透過結合青黴素結合蛋白（PBP）對不動桿菌屬 (Acinetobacter) 具有內在活性。與 ampicillin 合併使用時，可擴大對產 β-內醯胺酶的金黃色葡萄球菌、厭氧菌及革蘭氏陰性菌的涵蓋範圍。

細菌性（化膿性）關節炎的常見致病菌包括金黃色葡萄球菌等，與 Sulbactam 原有的抗感染適應症（金黃色葡萄球菌與大腸桿菌感染）高度重疊。這個很高的預測分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據。

需注意，此關聯是由類別藥理推論而來，而非有明確整理的機轉資料；且高分主要反映與既有適應症的相近性，不等同於已有直接的療效證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下依證據類型優先排序，列出與主題較相關的文獻（多數文獻的分類尚待確認）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2677956](https://pubmed.ncbi.nlm.nih.gov/2677956/) | 1989 | 隨機對照試驗 | Pediatr Infect Dis J | 兒童軟組織與骨骼感染（含 11 例化膿性關節炎）隨機分組，比較 ampicillin/sulbactam 與 ceftriaxone |
| [3026009](https://pubmed.ncbi.nlm.nih.gov/3026009/) | 1986 | 隨機對照（開放性） | Rev Infect Dis | 骨、關節及軟組織感染，sulbactam＋ampicillin 與 cefotaxime 比較，樣本數小（13 對 9 例） |
| [3026018](https://pubmed.ncbi.nlm.nih.gov/3026018/) | 1986 | 臨床研究 | Rev Infect Dis | 9 名兒童骨髓炎／化膿性關節炎，以 sulbactam/ampicillin 靜脈注射後續接口服 sultamicillin 序貫治療，致病菌皆對該組合敏感 |
| [3252119](https://pubmed.ncbi.nlm.nih.gov/3252119/) | 1988 | 臨床試驗 | Mikrobiyol Bul | 84 名各類感染患者（含 5 例化膿性關節炎與骨髓炎）接受 ampicillin＋sulbactam 治療 |
| [9263167](https://pubmed.ncbi.nlm.nih.gov/9263167/) | 1997 | 病例報告 | J Rheumatol | 貓咬傷後多殺巴斯德菌關節炎合併痛風，經 ampicillin/sulbactam 治療後感染緩解、關節功能恢復 |
| [1745624](https://pubmed.ncbi.nlm.nih.gov/1745624/) | 1991 | 體外比較／回顧 | Pharmacotherapy | 比較 ampicillin-sulbactam 與 ticarcillin-clavulanate 的體外活性與臨床療效 |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | 回顧 | Int J Antimicrob Agents | 多重抗藥菌感染中，新舊抗生素的仿單外使用與正式建議之比較 |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | 回溯性研究 | Clin Lab | 幼童骨關節感染的致病菌分布與抗藥性分析 |

說明：上述文獻多為 1980–1990 年代的小規模研究，且該批文獻的相關性標記尚待人工確認，尚無近年的高品質對照試驗。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-27636 | UNASYN 750 FOR INJ | 注射劑 | 未提供 |
| HK-32893 | SULPERAZON FOR INJ 500MG/500MG | 注射劑 | 未提供 |
| HK-56070 | KINTAMVY FOR INJ 0.75G | 注射劑 | 未提供 |
| HK-56071 | KINTAMVY FOR INJ 1.5G | 注射劑 | 未提供 |
| HK-56893 | NASPALUN FOR INTRAVENOUS INJ | 注射劑 | 未提供 |

共 8 張有效單方許可證（上表僅列 5 張，另有 XACDURO、SITANDING 及頭孢哌酮／舒巴坦產品）。劑型與核准適應症文字在許可證資料中均為空白。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物與疾病關係資料，非仿單文字）：腎臟疾病、輸尿管積膿、困難梭菌結腸炎、新生兒壞死性腸炎、傳染性單核球增多症、慢性 EB 病毒感染症候群。

其他警語、禁忌症與藥物交互作用資料目前缺乏，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- Sulbactam（多與 ampicillin 合併）已在香港上市，且有數項針對骨關節感染（含化膿性關節炎）的小型臨床研究，機轉上合理。但證據多屬早期、小規模研究，無臨床試驗登記，目前僅屬 L3，宜視為待驗證的研究問題。

**若要推進需要：**
- 人工審閱文獻，確認各研究中化膿性關節炎的獨立療效數據
- 取得香港原廠仿單，確認核准適應症、警語與禁忌症
- 補充作用機轉與抗藥性（如不動桿菌、MRSA）資料
- 評估與現行標準療法（如 cefazolin、頭孢菌素類）相比的定位與必要性
- 腎功能不全等高風險族群的安全性與劑量調整計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

