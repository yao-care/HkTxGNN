---
layout: default
title: Levocarnitine
parent: 僅模型預測 (L5)
nav_order: 524
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Levocarnitine：預測新適應症為類風濕性關節炎 (Rheumatoid Arthritis)（證據等級 L5）。原適應症：香港許可證資料未登載核准適應症"
monitor_inn: "LEVOCARNITINE"
predicted_indications: ["autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy", "rheumatoid arthritis", "sclerosing cholangitis"]
---

# Levocarnitine
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

# Levocarnitine：從（原適應症未登載）到類風濕性關節炎

## 一句話總結

Levocarnitine（左旋肉鹼）在香港已有 4 張有效許可證，但資料中未登載核准適應症。
TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效（預測分數 99.87%）。
目前僅有 **1 個 Phase 2 臨床試驗**，且該試驗的標題與內容顯示研究的是修格蘭氏症候群的乾眼症，與類風濕性關節炎的對應性需要再確認，**尚無文獻**直接支持。

> 說明：TxGNN 預測的第 1 名是「自體顯性家族性血尿-視網膜小動脈迂曲-攣縮症候群」（分數 99.94%），但完全沒有臨床或文獻證據，故本報告改以有實際研究線索的類風濕性關節炎為主軸，其他候選見下方補充。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未登載核准適應症 |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L2（僅 1 個小型 Phase 2 試驗，且與預測疾病的對應性有疑問；實際可信度偏低） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Levocarnitine 在體內負責將長鏈脂肪酸運送進粒線體進行 β 氧化，是細胞能量代謝的重要輔因子。

類風濕性關節炎患者常伴隨疲勞、血脂異常與粒線體功能異常，因此理論上，調節代謝與發炎的 levocarnitine 可能有輔助作用。不過這是推論，並非已確立的機轉。

要注意的是：該 Phase 2 試驗（NCT03953703）的標題是針對**修格蘭氏症候群的乾眼症**，與類風濕性關節炎並不相同。兩者同屬自體免疫疾病，但試驗並不能直接證明對類風濕性關節炎有效。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03953703](https://clinicaltrials.gov/study/NCT03953703) | Phase 2 | 已完成 | 15 | 隨機、安慰劑對照、雙盲交叉先導試驗，評估 levocarnitine 對修格蘭氏症候群乾眼症的效果；尚無公布結果 |

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-39342 | CARNITOR INJ 1G/5ML | 未登載 | 未登載 |
| HK-41015 | CARNITOR TAB 330MG | 未登載 | 未登載 |
| HK-36344 | CARNITENE SOLUTION 30% | 未登載 | 未登載 |
| HK-67686 | INESTOM PEDIATRIC ORAL SOLUTION 300MG/ML | 未登載 | 未登載 |

## 安全性考量

- **知識圖譜中的禁忌關聯**（來自 TxGNN 知識圖譜，非仿單內容）：癲癇、腎臟病、輸尿管積膿、肝病、膽囊疾病、低血壓疾病、凝血疾病、膽汁鬱積（含良性復發性肝內膽汁鬱積、家族性肝內膽汁鬱積）。
- **藥物交互作用**：共查得 68 筆。
  - 中度：Warfarin、Dicoumarol（抗凝血劑，需留意凝血功能監測）。
  - 其餘多數分級為未知，例如 Valproic acid、Topiramate、Digoxin、Metoprolol、Amlodipine 等。

完整警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一的臨床試驗規模很小（n=15），且研究的疾病為修格蘭氏症候群乾眼症，無法證明對類風濕性關節炎有效。
- 其餘預測候選也證據薄弱：糖尿病腎病變僅有 1 篇合併療法研究（levocarnitine 與 alprostadil 併用，無法分離單一藥物貢獻，證據等級 L4，列為研究問題）；其餘 3 個候選（含排名第 1、第 2 的 COL4A1 相關罕見血管疾病與硬化性膽管炎）僅有模型預測（L5）。

**若要推進需要：**
- 釐清 NCT03953703 的實際研究對象與主要終點，並取得試驗結果。
- 取得 levocarnitine 的作用機轉資料，以及香港許可證的核准適應症與仿單警語、禁忌。
- 若考慮糖尿病腎病變方向，需取得 PMID 41884608 的完整設計與樣本數，並尋找 levocarnitine 單藥的對照研究。
- 針對類風濕性關節炎進行文獻回顧，必要時設計專屬的小型概念驗證試驗。
- 若以腎病變族群為目標，需先評估腎功能不全與抗凝血劑併用的安全性監測計畫。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

