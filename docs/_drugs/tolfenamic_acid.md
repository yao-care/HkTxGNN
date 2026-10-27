---
layout: default
title: Tolfenamic Acid
parent: 高證據等級 (L1-L2)
nav_order: 887
evidence_level: L2
indication_count: 5
last_modified_at: 2026-10-14
description: "Tolfenamic Acid：預測新適應症為頭痛疾患 (Headache Disorder)（證據等級 L2）。原適應症：許可證未載明適應症"
monitor_inn: "TOLFENAMIC ACID"
predicted_indications: ["headache disorder", "tendinitis", "rheumatoid arthritis", "trigeminal autonomic cephalalgia", "idiopathic granulomatous myositis"]
---

# Tolfenamic Acid
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

## Tolfenamic Acid：從（原適應症資料缺漏）到頭痛疾患
{: .text-alpha }

## 一句話總結

Tolfenamic acid 是一種非類固醇消炎藥（NSAID），已在香港取得許可證（獸用製劑），本次資料中未載明原核准適應症。
TxGNN 模型預測它可能對**頭痛疾患 (Headache Disorder)** 有效，
目前**無登記臨床試驗**，但有 **20 篇文獻**支持這個方向，其中包含多項偏頭痛的隨機雙盲對照研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明適應症 |
| 預測新適應症 | 頭痛疾患 (Headache Disorder) |
| TxGNN 預測分數 | 99.74% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供）。根據文獻，tolfenamic acid 是前列腺素合成的強效抑制劑（抑制環氧合酶 COX），並有報告指出它對白三烯也有影響。前列腺素會使痛覺受器敏感化、參與血小板凝集與血管擴張，被認為與偏頭痛的病理機轉有關，因此機轉上合理。

在英國，本藥已被核准用於治療急性偏頭痛，在部分國家則僅限獸用。頭痛疾患與其說是「新」適應症，不如說是已有臨床使用基礎的方向，因此推進重點在於法規與確認性證據，而非從零驗證。

另有藥理資料顯示本藥可作用於 AKR1C3 這個標靶，但其與頭痛療效的關聯尚不明確。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下表為頭痛疾患（以偏頭痛為主）的主要文獻，依 RCT、Review、其他的順序排列。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2375249](https://pubmed.ncbi.nlm.nih.gov/2375249/) | 1990 | RCT | Acta Neurol Scand | 雙盲交叉試驗，比較 tolfenamic acid 200/400 mg 與 paracetamol 治療無預兆偏頭痛急性發作 |
| [3727918](https://pubmed.ncbi.nlm.nih.gov/3727918/) | 1986 | RCT | Acta Neurol Scand | 31 位患者；預防性使用 tolfenamic acid 與 propranolol 皆顯著減少發作次數與持續時間（相較安慰劑） |
| [6394143](https://pubmed.ncbi.nlm.nih.gov/6394143/) | 1984 | RCT | Cephalalgia | 比較 tolfenamic acid、metoclopramide、caffeine 及其組合治療偏頭痛發作 |
| [7816790](https://pubmed.ncbi.nlm.nih.gov/7816790/) | 1994 | Review | Pharmacol Toxicol | 回顧 tolfenamic acid 在偏頭痛急性與預防性治療的角色 |
| [7816789](https://pubmed.ncbi.nlm.nih.gov/7816789/) | 1994 | Review | Pharmacol Toxicol | 探討偏頭痛與前列腺素、白三烯的關係 |
| [1495823](https://pubmed.ncbi.nlm.nih.gov/1495823/) | 1992 | Review | Pathol Biol | 回顧 NSAID（含 tolfenamic acid）用於偏頭痛急性與預防治療的對照研究 |
| [8749241](https://pubmed.ncbi.nlm.nih.gov/8749241/) | 1995 | Review | Cephalalgia | 回顧急性偏頭痛發作中止痛藥與 NSAID 的使用 |
| [9563211](https://pubmed.ncbi.nlm.nih.gov/9563211/) | 1998 | 隨機對照試驗（分類待定） | Headache | 141 位患者；速釋型 tolfenamic acid 與口服 sumatriptan 在急性偏頭痛的療效相當 |
| [12474702](https://pubmed.ncbi.nlm.nih.gov/12474702/) | 2002 | 隨機雙盲試驗（分類待定） | Medicina (Kaunas) | 192 位患者；比較 tolfenamic acid 300 mg 與 pizotifen 預防偏頭痛 |
| [89390](https://pubmed.ncbi.nlm.nih.gov/89390/) | 1979 | 雙盲交叉試驗（分類待定） | Lancet | tolfenamic acid 與 ergotamine 效果相當，且噁心等副作用較少 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-50767 | TOLFEDINE TAB 20MG (VET) | 未載明 | 未載明（品名標示為獸用製劑） |

## 安全性考量

- **藥物交互作用**：藥理資料顯示本藥與 AKR1C3 有標靶層級的作用，但並非具臨床意義的藥物間交互作用，且未提供嚴重度分級。
- 文獻中另有與 sumatriptan、rizatriptan 併用以降低偏頭痛復發的研究，以及與 ergotamine 濫用相關的報告，臨床使用時值得留意。

其餘安全性資訊（警語、禁忌症）請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多項針對偏頭痛的隨機雙盲對照研究（對照 paracetamol、propranolol、sumatriptan、pizotifen 等），機轉（抑制前列腺素合成）也合理，且本藥在部分地區已用於偏頭痛。
- 但這些研究多為 1980–1990 年代的舊資料，無登記臨床試驗，樣本數與終點無法僅憑摘要確認；香港許可證亦為獸用製劑，因此證據等級保守定為 L2。

**若要推進需要：**
- 取得香港許可證的完整仿單，補齊警語、禁忌症與適應症資料
- 釐清香港獸用製劑與人用頭痛適應症之間的法規路徑，目前許可證並不涵蓋人用
- 逐篇查證主要 RCT 的樣本數、終點與統計結果，確認可否達到更高證據等級
- 補充詳細作用機轉資料（MOA）
- 擬定 NSAID 類藥物的消化道與心血管安全性監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

