---
layout: default
title: Bisoprolol
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Bisoprolol：預測新適應症為惡性高血壓性腎病 (Malignant Hypertensive Renal Disease)（證據等級 L5）。原適應症：高血壓"
monitor_inn: "Bisoprolol"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Bisoprolol
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

# Bisoprolol：從高血壓到惡性高血壓性腎病

## 一句話總結

Bisoprolol 是選擇性 β1 受體阻斷劑，原本用於高血壓治療。
TxGNN 模型預測它可能對**惡性高血壓性腎病 (Malignant Hypertensive Renal Disease)** 有效，
但目前**沒有臨床試驗**，也沒有直接相關的文獻，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓（來自知識圖譜的適應症資料；香港許可證未載明核准適應症文字） |
| 預測新適應症 | 惡性高血壓性腎病 (Malignant Hypertensive Renal Disease) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 18 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Bisoprolol 是 β1 選擇性阻斷劑，其降血壓療效在高血壓中已被證實。β1 阻斷可降低血壓並減少腎素釋放，機轉上與惡性高血壓性腎病有合理的連結。

惡性高血壓性腎病是高血壓控制不良所引起的嚴重併發症，因此與原適應症在疾病譜上相近。不過，惡性高血壓通常需要快速的靜脈降壓治療，口服 β 阻斷劑並非標準第一線選擇。TxGNN 的高分（99.94%）可能主要反映它與已核准高血壓適應症的相似性，而非獨立的療效證據。

其他排名較前的預測也屬同一類型：

- **惡性腎血管性高血壓**：分數 99.94%。β1 阻斷可減少腎素分泌，理論上相關，但屬推論；血管重建術與 RAAS 抑制劑等疾病專屬處置優先。
- **肺高壓（機轉不明的多因素型）**：分數 99.93%。現有資料不支持直接的機轉依據，預測可能源於疾病名稱中共有的「hypertension」一詞。β 阻斷劑用於肺動脈高壓需謹慎，因可能抑制右心室功能。
- **肺高壓（肺部疾病/缺氧所致）**：分數 99.93%。目前僅有間接的文獻背景。
- **Braddock 症候群**：分數 99.91%。無任何機轉或研究支持，僅為運算預測。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對首位預測（惡性高血壓性腎病）目前無相關文獻。

下表為排名第 4 的預測「肺高壓（肺部疾病/缺氧所致）」所檢索到的文獻，僅提供間接背景，**並非** Bisoprolol 用於肺高壓或本報告首位預測的臨床證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Review | Cardiovasc Drugs Ther | 探討 β 阻斷劑對心衰竭患者肺功能的影響，過去認為肺功能受損者不宜使用，近年此觀念受到挑戰 |
| [23506636](https://pubmed.ncbi.nlm.nih.gov/23506636/) | 2013 | 臨床比較（心衰竭） | Int J Cardiol | 比較 carvedilol、bisoprolol、nebivolol 在中度心衰竭的多參數表現 |
| [18845967](https://pubmed.ncbi.nlm.nih.gov/18845967/) | 2008 | 生理學研究 | Med Sci Sports Exerc | 探討 β 阻斷與代謝化學反射對運動能力的影響 |
| [23706341](https://pubmed.ncbi.nlm.nih.gov/23706341/) | 2013 | 生理學研究 | J Am Soc Echocardiogr | 以斑點追蹤心臟超音波研究急性缺氧下左心室功能，並比較有無 β1 阻斷 |
| [32363697](https://pubmed.ncbi.nlm.nih.gov/32363697/) | 2020 | 前臨床 | Fundam Clin Pharmacol | Bisoprolol 經 PI3K/AKT/GSK3β 路徑保護心肌細胞免於缺血再灌注損傷 |
| [27687650](https://pubmed.ncbi.nlm.nih.gov/27687650/) | 2016 | 前臨床（體外） | Nan Fang Yi Ke Da Xue Xue Bao | 探討 bisoprolol 預處理對 H9c2 心肌細胞缺氧/復氧損傷的作用 |
| [39088923](https://pubmed.ncbi.nlm.nih.gov/39088923/) | 2024 | 前臨床（動物） | Int Immunopharmacol | Diosmin 合併 bisoprolol 減輕氯化鈷誘發的心臟毒性與內皮功能障礙 |
| [12887136](https://pubmed.ncbi.nlm.nih.gov/12887136/) | 2003 | Case report | Hypertens Res | 兩例合併法洛氏四重症的嗜鉻細胞瘤病例 |

## 香港上市資訊

本藥在香港共有 18 張有效許可證（皆為單方，無已註銷者），許可證資料中未載明劑型與核准適應症。主要許可證如下：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-29917 | CONCOR 5 FILM-COATED TAB 5MG | 未載明 | 未載明 |
| HK-48662 | CONCOR TAB 2.5MG | 未載明 | 未載明 |
| HK-63998 | BISO TABLETS 5MG | 未載明 | 未載明 |
| HK-55559 | APO-BISOPROLOL TAB 5MG | 未載明 | 未載明 |
| HK-67481 | BISOCORD 5 TABLETS 5MG | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜中的疾病禁忌關聯**（非仿單文字）：腎臟疾病、肝臟疾病、氣喘（含內因性與過敏性）、糖尿病及糖尿病酮酸中毒、全身性紅斑性狼瘡、乾癬、痛風、胰臟炎、膽囊疾病、肝昏迷/肝性腦病變、重症肌無力、無尿、焦慮症、低鉀相關疾病、高血鈣、副甲狀腺功能亢進等。
- **藥物交互作用**：共查得 100 筆，以下為部分結果。
  - 中度：Epinephrine、Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide、Bupropion、Morphine、Atropine、Hyoscyamine、Methscopolamine、Acetohexamide，以及多種鈣鹽（碳酸鈣、醋酸鈣、檸檬酸鈣、葡萄糖酸鈣等）
  - 輕微：Acetylsalicylic acid、Aluminum hydroxide、Attapulgite

此外，β 阻斷劑用於肺高壓相關預測時，需特別留意可能的右心室功能抑制與呼吸道風險。其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測皆為 L5，沒有任何臨床試驗或直接文獻，高分可能只反映與已核准高血壓適應症的相似性。
- 惡性高血壓性腎病通常需要快速的靜脈降壓處置，口服 Bisoprolol 並非標準選擇；肺高壓方向則有安全性疑慮。

**若要推進需要：**
- 取得 Bisoprolol 的作用機轉資料（MOA）
- 取得香港原廠仿單的警語、禁忌與核准適應症
- 針對惡性高血壓性腎病或腎血管性高血壓，進行系統性文獻回顧，確認是否有直接的臨床證據
- 若有初步證據，再設計小規模探索性研究，並納入腎功能、血壓與心率的監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

