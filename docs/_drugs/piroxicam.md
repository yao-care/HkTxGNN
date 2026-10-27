---
layout: default
title: Piroxicam
parent: 僅模型預測 (L5)
nav_order: 707
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Piroxicam：預測新適應症為科羅波瑪性小眼症-根性肢體發育不良症候群 (colobomatous microphthalmia-rhizomelic dysplasi…（證據等級 L5）。原適應症：類風濕性關節炎、骨關節炎、關節病變"
monitor_inn: "PIROXICAM"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis"]
---

# Piroxicam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Piroxicam：從類風濕性關節炎到先天性骨骼與肢體發育異常症候群（預測）
{: .text-alpha }

## 一句話總結

Piroxicam 是一種非類固醇消炎止痛藥（NSAID），原本用於類風濕性關節炎、骨關節炎等關節疾病。
TxGNN 模型預測它可能對**科羅波瑪性小眼症-根性肢體發育不良症候群 (colobomatous microphthalmia-rhizomelic dysplasia syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 類風濕性關節炎、骨關節炎、關節病變（來自知識圖譜，香港許可證未載明適應症文字） |
| 預測新適應症 | 科羅波瑪性小眼症-根性肢體發育不良症候群 (colobomatous microphthalmia-rhizomelic dysplasia syndrome) |
| TxGNN 預測分數 | 99.996% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Piroxicam 屬於非選擇性 COX 抑制劑類的 NSAID，其在關節炎類疾病中的消炎止痛效果已被廣泛使用，但機轉上並無明確證據顯示適用於預測的新適應症。

預測的新適應症是罕見的先天性發育異常症候群，推測為基因性病因，沒有已知由 COX／前列腺素驅動的病理機制可供 Piroxicam 作用。0.99996 的高分較可能反映知識圖譜中的網路相似性，而非生物學上的合理性。

同一批預測還包括另外四個疾病，分數相近（99.99%），整體判斷如下：

| 排名 | 預測疾病 | 分數 | 機轉關聯評估 |
|------|---------|------|-------------|
| 2 | 短指-併指症候群 (brachydactyly-syndactyly syndrome) | 99.996% | 無；先天性肢體畸形，消炎無法矯正結構缺陷 |
| 3 | 肢中發育不良，Hunter-Thompson 型 (acromesomelic dysplasia, Hunter-Thompson type) | 99.996% | 無；與 GDF5 訊號路徑缺陷相關，COX 抑制不作用於此路徑 |
| 4 | 短軀幹-牙釉質發育不全症候群 (brachyolmia-amelogenesis imperfecta syndrome) | 99.996% | 無；NSAID 對牙釉質形成與骨骼生長無已知影響 |
| 5 | 肌硬化症 (myosclerosis) | 99.995% | 僅有微弱、推測性的關聯（肌肉纖維化可能伴隨發炎，NSAID 理論上可緩解症狀）；若要探索，此項最合理 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 20 張有效的單方許可證，無已註銷者。許可證資料中未載明劑型與核准適應症文字。以下列出 5 張主要許可證：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-62392 | POZZIE GEL 1%W/W | WELLDONE PHARMACEUTICALS LIMITED |
| HK-55642 | PHARMOR TORICAM GEL 10MG/G | WILSON TRADING COMPANY LIMITED |
| HK-66650 | PIRADEN GEL 0.5% W/W | DELTAPHARM LIMITED |
| HK-37734 | ROSIDEN INJ 20MG/ML | JULIUS CHEN & COMPANY (HK) LIMITED |
| HK-45432 | CP-PIROX 20 CAP 20MG | CHRISTO PHARM LTD |

從品名可見，香港上市產品包含外用凝膠、注射劑、膠囊與錠劑等多種型態。

## 安全性考量

- **知識圖譜中的禁忌疾病**（非仿單文字，僅供參考）：高血壓、腎臟疾病、肝臟疾病（含急性肝衰竭、肝炎、藥物性肝損傷）、膽囊疾病、充血性心衰竭、心肌梗塞與其他心血管疾病、中風與腦血管疾病、凝血疾病、活動性消化性潰瘍、貧血、血紅素病變、物質濫用／依賴、視覺障礙，以及血栓性疾病。
- **藥物交互作用**：資料庫共查得 100 筆交互作用，以下為部分範例：
  - 中度：阿斯匹靈 (Acetylsalicylic acid)、Metformin、Glimepiride、Chlorpropamide、多種皮質類固醇（Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide）、Mesalazine、Balsalazide、Aprepitant、檸檬酸鉀、碳酸氫鉀
  - 輕度：Famotidine、Ranitidine、Cimetidine、Linaclotide

仿單的警語與禁忌資訊尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 五個預測適應症皆只有模型分數，沒有臨床試驗或文獻，且多為基因性先天發育異常，與 COX 抑制的機轉缺乏關聯，高分很可能是網路相似性造成的假象。
- 作用機轉資料缺漏，且仿單安全性資訊尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 補齊 Piroxicam 的作用機轉資料（如查詢 DrugBank）
- 下載並解析香港衛生署的仿單，取得警語與禁忌症
- 若仍想探索，優先針對肌硬化症 (myosclerosis) 做文獻回顧與機轉驗證，再評估是否值得進行前臨床研究
- 對其餘四個先天發育異常症候群，除非找到明確的生物學證據，否則不建議投入資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

