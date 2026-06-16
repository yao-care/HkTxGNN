---
layout: default
title: Cisatracurium
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
---

# Cisatracurium
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

# Cisatracurium：從麻醉肌鬆到馬尾症候群

## 一句話總結

Cisatracurium 是非去極化神經肌肉阻斷劑（NMBA），廣泛用於全身麻醉插管及加護病房的骨骼肌鬆弛管理。
TxGNN 模型預測它可能對**馬尾症候群 (Cauda Equina Syndrome)** 有效，預測分數高達 **99.99%**。
然而，目前**無任何臨床試驗或文獻**支持此方向，機轉分析顯示此預測極可能為脊椎手術麻醉情境共現所致的假陽性信號。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 麻醉及 ICU 神經肌肉阻斷（香港未上市，無許可證紀錄） |
| 預測新適應症 | 馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Cisatracurium 屬苯甲基異喹啉類非去極化 NMBA，作用機轉為競爭性拮抗骨骼肌神經肌肉接點（NMJ）的菸鹼型乙醯膽鹼受體（nAChR），產生可逆性骨骼肌鬆弛效果。相較於同類藥物 atracurium，cisatracurium 具有極低的組胺釋放，心血管副作用顯著減少，因此在高風險手術及重症加護病房中廣泛應用。目前尚缺乏更完整的 MOA 文件（Data Gap DG002）。

馬尾症候群（Cauda Equina Syndrome, CES）為腰椎管內馬尾神經根受壓迫的結構性急症，典型表現為雙下肢無力、鞍區感覺障礙及括約肌功能喪失。其治療核心為緊急外科減壓手術，無任何藥物可替代。

**此預測機轉上難以成立。** NMBA 僅作用於周邊骨骼肌 NMJ，不穿越血腦屏障，亦無神經減壓、神經保護或脊椎結構修復機轉。Evidence Pack 的機轉分析指出，TxGNN 的高分預測最可能源自「脊椎手術麻醉情境共現（confounding by surgical context）」——Cisatracurium 作為脊椎減壓手術的常規肌鬆用藥，與 CES 患者在知識圖譜中節點相鄰，但這屬於情境性混淆，而非因果關聯，不支持再利用假說。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
馬尾症候群為神經外科急症，標準治療為手術而非藥物；Cisatracurium 作為 NMBA 對 CES 病理無任何直接作用機轉。TxGNN 的高預測分數（99.99%）為手術情境共現所產生的偽信號，而非真實再利用機會。香港無上市紀錄、無臨床試驗、無支持性文獻，且所有安全性資料均缺失，不具備推進條件。

**若要推進需要：**
- 先排除情境性混淆假說，確認是否存在獨立的生物學機轉假設
- 取得香港原廠仿單，補充完整警語與禁忌資訊（Data Gap DG001）
- 補充藥物詳細作用機轉資料（Data Gap DG002）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

