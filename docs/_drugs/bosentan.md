---
layout: default
title: Bosentan
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 9
---

# Bosentan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Bosentan：從肺動脈高壓到類風濕性關節炎

## 一句話總結

Bosentan 是一種內皮素受體拮抗劑，臨床上主要用於肺動脈高壓（PAH）。
TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效。
目前**沒有任何 RA 的臨床試驗**，僅有 **2 篇小鼠關節炎動物研究**支持機轉，屬於研究假說階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肺動脈高壓（香港許可證資料未載明適應症文字，此項依證據包文獻與說明推得） |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.80% |
| 證據等級 | L4（僅有前臨床研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位尚未取得）。Bosentan 是雙重內皮素受體（ETA/ETB）拮抗劑，其在 PAH 的療效已被證實。內皮素-1（ET-1）除了收縮血管，也參與發炎反應，因此機轉上可能適用於 RA。

前臨床研究提供了間接支持。小鼠的膠原蛋白誘發關節炎（CIA）與 zymosan 誘發關節炎模型顯示，內皮素系統與 TNF-α、LTB4 及關節痛覺過敏有關。文獻也指出 RA 病人的血漿與滑膜中 ET-1 濃度升高。

但這些證據都停留在動物實驗。目前沒有 RA 病人的臨床資料，其餘文獻多為結締組織病相關 PAH 的回顧，與 RA 本身的療效無直接關係。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06957002](https://clinicaltrials.gov/study/NCT06957002) | Phase 2 | 尚未招募 | 40 | 巨細胞動脈炎（非 RA）：比較 Bosentan 加糖皮質素與單用糖皮質素，主要指標為 12 個月無失敗存活率 |

此試驗研究的是另一種疾病，只能顯示 Bosentan 在風濕性血管炎領域受到關注，沒有提供 RA 的資料。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22249931](https://pubmed.ncbi.nlm.nih.gov/22249931/) | 2012 | 前臨床（動物） | Inflammation Research | Bosentan 可改善小鼠膠原蛋白誘發關節炎，TNF-α 參與內皮素系統基因的誘導 |
| [18515326](https://pubmed.ncbi.nlm.nih.gov/18515326/) | 2008 | 前臨床（動物） | Journal of Leukocyte Biology | 內皮素受體拮抗可調節 zymosan 誘發關節炎的嗜中性球聚集與水腫，涉及 LTB4、TNF-α、CXCL-1 |
| [24268012](https://pubmed.ncbi.nlm.nih.gov/24268012/) | 2014 | Review | Rheumatic Diseases Clinics of North America | 結締組織病相關 PAH 的回顧，首年死亡率可達 10–15% |
| [16218473](https://pubmed.ncbi.nlm.nih.gov/16218473/) | 2005 | Review | Lupus | 結締組織病相關 PAH 的回顧，RA 為較少見的相關疾病 |
| [19487226](https://pubmed.ncbi.nlm.nih.gov/19487226/) | 2009 | Review | Rheumatology (Oxford) | 血管病變與 PAH 的臨床表現及處置 |
| [16766656](https://pubmed.ncbi.nlm.nih.gov/16766656/) | 2006 | 前臨床（動物，非 Bosentan 專一） | PNAS | IL-15 引發的痛覺過敏，與 IFN-γ、內皮素、前列腺素的連續釋放有關，並被雙重內皮素受體拮抗劑抑制 |
| [20054770](https://pubmed.ncbi.nlm.nih.gov/20054770/) | 2009 | Case report | Kardiologia Polska | 艾森曼格症候群合併幼年型類風濕性關節炎的女童，使用 Bosentan 治療 PAH 後臨床改善 |
| [25274237](https://pubmed.ncbi.nlm.nih.gov/25274237/) | 2014 | Case report | Internal Medicine | 修格連氏症候群相關 PAH 病人，由靜脈 epoprostenol 轉為含 Bosentan 的口服合併療法 |
| [16766376](https://pubmed.ncbi.nlm.nih.gov/16766376/) | 2006 | 臨床研究 | Scandinavian Journal of Rheumatology | 原發性修格連氏症候群合併 PAH 的臨床特徵與內皮素受體拮抗劑（無摘要） |
| [19969421](https://pubmed.ncbi.nlm.nih.gov/19969421/) | 2010 | 前臨床（動物，非 Bosentan 專一） | Pain | IL-17 參與小鼠抗原誘發關節炎的關節痛覺過敏 |

以上文獻沒有任何一篇是 Bosentan 治療 RA 的臨床研究。

---

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-65646 | PULMONAT TABLETS 125MG | I & C (HONG KONG) LIMITED |
| HK-65770 | ACCORD BOSENTAN TABLETS 125MG | JACOBSON MARKETING LIMITED |
| HK-66964 | PULMIFEX TABLETS 125MG | JACOBSON MARKETING LIMITED |
| HK-67787 | BOSENTAN TABLETS 125MG | SINO PACIFIC PHARMA COMPANY LIMITED |
| HK-65124 | PMS-BOSENTAN TABLETS 125MG | DCH AURIGA (HONG KONG) LIMITED - HEALTHCARE DIVISION |

以上為 10 張許可證中的 5 張。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- RA 的預測分數雖高，但證據僅有小鼠模型，沒有 RA 臨床資料，屬於證據等級 L4 的研究假說。
- 證據包缺少香港衛生署仿單的警語與禁忌資料，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌資料（目前為阻斷性缺口）。
- 補齊 DrugBank 作用機轉資料。
- 尋找或設計 RA 病人的臨床研究，例如探索性的 Phase 2 試驗。

**補充：**同一份預測清單中，**限制型系統性硬化症 (Limited Systemic Sclerosis)**（排名第 3，分數 99.65%）的證據明顯較強，等級為 L2，建議為 Proceed with Guardrails。證據包含 2023 年關於指端潰瘍的系統性回顧、多篇 SSc-PAH 回顧、2024 年葡萄牙 Raynaud 現象與指端潰瘍建議，以及一項 300 人的觀察性研究（NCT05168215，狀態未知）。不過並非所有研究結果一致，一項小型研究（PMID 19350343）未發現微血管改善。若要優先投入資源，建議先評估這個適應症，並落實肝毒性監測、致畸胎風險與避孕管控，以及藥物交互作用審查。

*本報告僅供研究參考，不構成醫療建議；藥物再利用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

