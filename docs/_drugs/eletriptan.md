---
layout: default
title: Eletriptan
parent: 高證據等級 (L1-L2)
nav_order: 230
evidence_level: L2
indication_count: 4
---

# Eletriptan
{: .fs-9 }

證據等級: **L2** | 預測適應症: **4** 個
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

# Eletriptan：從偏頭痛到腦幹先兆偏頭痛

## 一句話總結

Eletriptan（Relpax）是一種第二代 triptan 類藥物，屬 5-HT₁B/₁D 受體促效劑，原本用於急性偏頭痛（含或不含先兆）的治療。TxGNN 模型預測它可能對**腦幹先兆偏頭痛 (Migraine with Brainstem Aura)** 這一特定亞型有效，目前有 **0 個臨床試驗**和 **18 篇文獻**（主要針對一般偏頭痛）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性偏頭痛（含或不含先兆） |
| 預測新適應症 | 腦幹先兆偏頭痛 (Migraine with Brainstem Aura) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Eletriptan 是一種強效、選擇性的 5-HT₁B/₁D 受體促效劑。相較於第一代 triptan（sumatriptan），它對 5-HT₁D 受體的親和力高 6 倍、對 5-HT₁B 受體高 3 倍。作用機轉上，eletriptan 透過活化三叉神經血管系統中的 5-HT₁B/₁D 受體，收縮擴張的顱內血管、抑制三叉神經末梢釋放 P 物質與 CGRP，從而減少神經源性發炎、終止偏頭痛發作。

腦幹先兆偏頭痛（舊稱「基底型偏頭痛」）是偏頭痛的特定亞型，其先兆症狀源自腦幹或雙側大腦皮質，表現為眩暈、複視、構音障礙、耳鳴等，後續常伴隨典型偏頭痛頭痛。由於其頭痛期的病理生理機轉仍以三叉神經血管系統為核心，eletriptan 的作用機轉在此亞型理論上具高度適用性，這與 TxGNN 預測的合理性高度吻合。

然而有一個重要安全性疑慮需要評估：腦幹先兆偏頭痛的先兆症狀可能反映基底動脈（後循環）區域的血管變化，使用 triptans 的血管收縮效果理論上存在加重後循環缺血的風險。傳統指引曾將此亞型列為 triptans 的相對禁忌，但近年文獻（包括 IHS 2013 診斷分類修訂）重新評估後認為實際風險可能被高估，此議題仍存在臨床爭議，是推進本預測最需謹慎應對的核心問題。

---

## 臨床試驗證據

目前無相關臨床試驗登記（針對「腦幹先兆偏頭痛」特定亞型）。

---

## 文獻證據

以下文獻涵蓋 eletriptan 用於一般偏頭痛（含先兆）的研究，為腦幹先兆偏頭痛亞型提供機轉外推基礎，依研究品質排序。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | 臨床實踐指引 | *Headache* | 美國頭痛學會急性偏頭痛藥物療法系統性證據評估，eletriptan 獲 A 級推薦 |
| [11844898](https://pubmed.ncbi.nlm.nih.gov/11844898/) | 2002 | RCT（Phase 3） | *European Neurology* | 雙盲 RCT 顯示 eletriptan 80mg 療效優於 ergotamine/caffeine，含先兆患者納入 |
| [12807526](https://pubmed.ncbi.nlm.nih.gov/12807526/) | 2003 | RCT | *Cephalalgia* | Eletriptan 40mg 對 sumatriptan 反應不佳患者有效（n=446，含先兆患者），雙盲安慰劑對照 |
| [15469451](https://pubmed.ncbi.nlm.nih.gov/15469451/) | 2004 | RCT | *European Journal of Neurology* | 先兆期給予 eletriptan 80mg 無法縮短先兆本身，確立其療效窗口在頭痛期（與腦幹先兆亞型評估直接相關） |
| [17501848](https://pubmed.ncbi.nlm.nih.gov/17501848/) | 2007 | RCT | *Headache* | Eletriptan 顯著改善急性偏頭痛患者的功能損害與工作生產力，多維度功能評估 |
| [11687056](https://pubmed.ncbi.nlm.nih.gov/11687056/) | 2001 | Cochrane 系統回顧 | *Cochrane Database* | Eletriptan 急性偏頭痛治療的 Cochrane 系統性評估，確立有效性與安全性基礎 |
| [12498013](https://pubmed.ncbi.nlm.nih.gov/12498013/) | 2002 | 藥物回顧 | *Curr Opin Investig Drugs* | Eletriptan 藥理學綜述，說明其相較 sumatriptan、zolmitriptan、naratriptan 的受體選擇性優勢 |
| [21028917](https://pubmed.ncbi.nlm.nih.gov/21028917/) | 2010 | Review | *Paediatric Drugs* | Triptans 兒童偏頭痛使用回顧，包含 eletriptan 的兒科安全性資料 |
| [25155004](https://pubmed.ncbi.nlm.nih.gov/25155004/) | 2014 | 病例報告 | *Rev Port Cardiol* | 有冠心病史患者服用 eletriptan 後發生 NSTEMI，強調心血管風險評估的必要性 |
| [11050304](https://pubmed.ncbi.nlm.nih.gov/11050304/) | 2000 | 藥理學研究（離體） | *European Journal of Pharmacology* | 比較 eletriptan 與 sumatriptan 對人類分離腦膜動脈與冠狀動脈的收縮效應，提供血管選擇性基礎數據 |

---

## 香港上市資訊

Eletriptan 目前在香港**未上市**，衛生署無相關藥品許可證登記。若計劃在香港推進，需啟動完整的藥品許可申請流程。

---

## 安全性考量

安全性資訊請參考原廠仿單（Pfizer Relpax®）。

> ⚠️ **腦幹先兆偏頭痛亞型特別注意事項**：此亞型使用 triptans 歷史上存在爭議，需特別排除有後循環 TIA/缺血性中風病史、未控制高血壓或嚴重心腦血管疾病的患者，並於使用前充分評估後循環血管收縮風險。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Eletriptan 的 5-HT₁B/₁D 機轉與腦幹先兆偏頭痛的三叉神經血管病理生理學具高度相關性，多個高品質 RCT 已建立其在一般偏頭痛（含先兆）的 L2 級療效證據。然而，目前缺乏針對腦幹先兆偏頭痛特定亞型的 RCT，且腦幹先兆偏頭痛使用 triptans 的安全性爭議尚未完全解決，需設定明確的患者篩選與監測護欄。

**若要推進需要：**
- 取得 eletriptan 完整仿單（確認腦幹先兆偏頭痛是否列為禁忌症或警語）
- 補充詳細 MOA 資料（DrugBank API 查詢）
- 系統性蒐集 triptans 用於腦幹先兆偏頭痛的真實世界安全性文獻（近 5 年更新）
- 制定明確患者排除標準：後循環 TIA/中風史、嚴重冠心病、未控制高血壓
- 確認香港衛生署藥品許可申請策略（目前未上市，需完整審批流程）
- 考慮以前瞻性觀察性研究或專科登記研究形式，收集此亞型的亞洲患者安全性數據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

