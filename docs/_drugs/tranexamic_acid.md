---
layout: default
title: Tranexamic Acid
parent: 中證據等級 (L3-L4)
nav_order: 895
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Tranexamic Acid：預測新適應症為閉經 (Amenorrhea)（證據等級 L4）。原適應症：子宮內膜異位症 (Endometriosis)"
monitor_inn: "TRANEXAMIC ACID"
predicted_indications: ["amenorrhea (disease)"]
---

# Tranexamic Acid
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Tranexamic Acid：從子宮內膜異位症到閉經

## 一句話總結

Tranexamic Acid（傳明酸）是一種抗纖維蛋白溶解藥物，原本在知識圖譜中的適應症為子宮內膜異位症（endometriosis）。
TxGNN 模型預測它可能對**閉經 (Amenorrhea)** 有關，但目前**沒有臨床試驗**，只有 **2 篇文獻**（均為綜述）間接相關。
此預測的機轉連結偏間接，建議視為待驗證的假說。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 子宮內膜異位症 (Endometriosis)（來自知識圖譜；香港許可證未提供適應症文字） |
| 預測新適應症 | 閉經 (Amenorrhea) |
| TxGNN 預測分數 | 99.19% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知藥理，Tranexamic Acid 是離胺酸（lysine）類似物，屬於抗纖維蛋白溶解劑，可阻斷纖維蛋白溶解酶原（plasminogen）與纖維蛋白的結合，減少由纖維蛋白溶解所驅動的經血流失。

因此，它在減少月經過多、以及血液腫瘤病患的經期預防或抑制（menses prophylaxis/suppression）上有合理的角色。不過，它**並不經由荷爾蒙或子宮內膜萎縮的機轉誘發閉經**。與閉經的關聯是間接的：藥物減少的是出血量，而不是治療或造成「月經消失」。

TxGNN 的高分（0.99）屬於計算模型預測，並沒有直接臨床資料支持。也應注意，閉經本身是一種症狀或狀態，是否為合適的治療目標需要重新界定，例如改以「異常子宮出血」或「月經過多」作為評估適應症，可能更貼近實際證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause | 異常子宮出血的藥物治療回顧；非荷爾蒙藥物（含 NSAIDs 等）可減少出血，用藥選擇取決於病因、出血量與生育需求 |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Review | J Oncol Pharm Pract | 停經前血液惡性腫瘤病患的經期預防與抑制之系統性處理方式；指出不同療法間缺乏比較資料 |

---

## 香港上市資訊

香港共有 20 張有效單方許可證，以下列出 5 張主要許可證（許可證資料未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-22792 | TRANSAMIN TAB 500MG（第一三共） | 錠劑 | 未提供 |
| HK-00708 | TRANSAMIN CAP 250 MG（第一三共） | 膠囊劑 | 未提供 |
| HK-00715 | TRANSAMIN INJ 5%（第一三共） | 注射劑 | 未提供 |
| HK-00704 | TRANSAMIN S INJ 10%（第一三共） | 注射劑 | 未提供 |
| HK-66670 | TRANSX SOLUTION FOR INJECTION/INFUSION 250MG/5ML | 注射／輸注液 | 未提供 |

---

## 安全性考量

- **藥物交互作用**：共查得 35 項交互作用，其中多項為 Major 等級，主要涉及：
  - 含雌激素或黃體素的荷爾蒙製劑（如 Ethinylestradiol、Estradiol、Conjugated estrogens、Norethisterone、Drospirenone、Etonogestrel 等），可能增加血栓風險
  - 凝血相關製劑（Anti-inhibitor coagulant complex、Factor IX Complex）
  - Carfilzomib
  - 溶栓劑（Alteplase、Anistreplase）為 Moderate 等級，因作用相反而需留意
- **知識圖譜標示的相關疾病風險**（非仿單文字，僅供參考）：血栓性靜脈炎、中風與腦血管疾病、冠狀動脈疾病、高血壓、糖尿病、肝病、卟啉症、子宮內膜癌與乳癌等。

仿單的警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，僅有 2 篇間接相關的綜述，證據等級為 L4。
- 藥物的機轉只能減少出血量，無法解釋「閉經」，高分預測缺乏直接支持。
- 若與荷爾蒙製劑併用（用於經期抑制時很常見），血栓風險須嚴格評估。

**若要推進需要：**
- 重新界定適應症，例如改評估月經過多或異常子宮出血、血液腫瘤病患的經期管理
- 補齊作用機轉（MOA）資料
- 取得香港原廠仿單的警語、禁忌症與核准適應症
- 針對血液腫瘤病患的經期抑制，蒐集前瞻性或回溯性資料
- 制定併用荷爾蒙製劑時的血栓風險評估與監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

