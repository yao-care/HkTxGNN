---
layout: default
title: Aztreonam
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
---

# Aztreonam
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

# Aztreonam：從革蘭氏陰性菌感染到多株性高黏滯症候群

## 一句話總結

Aztreonam 是單環 β-內醯胺類（monobactam）抗生素，資料中未載明原適應症。
TxGNN 預測分數最高的新適應症是**多株性高黏滯症候群 (Polyclonal Hyperviscosity Syndrome)**，但**沒有任何臨床試驗或文獻支持**，機轉上也無合理關聯，屬純模型預測。
在前 10 名預測中，證據最多的是**淋球菌性尿道炎 (Gonococcal Urethritis)**：1 個已完成的 Phase 2/3 試驗與 8 篇文獻，詳見後文補充章節。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症（Aztreonam 為抗菌藥，用於革蘭氏陰性菌感染） |
| 預測新適應症 | 多株性高黏滯症候群 (Polyclonal Hyperviscosity Syndrome) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Aztreonam 抑制細菌 PBP3（青黴素結合蛋白 3），阻斷細胞壁合成，主要對革蘭氏陰性菌有效。

**這個預測在機轉上不合理。** Aztreonam 對血漿蛋白濃度或血液黏稠度沒有已知作用，原適應症（細菌感染）與高黏滯症候群也沒有關聯。分數高（99.73%）但沒有任何臨床或文獻佐證，較可能是知識圖譜的統計假象。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 補充：證據較充分的預測適應症

以下依 TxGNN 前 10 名預測整理。除淋球菌性尿道炎外，其餘證據都不足。

| 排名 | 預測適應症 | 分數 | 證據等級 | 評估 |
|------|-----------|------|---------|------|
| 2 | 高澱粉酶血症 (Hyperamylasemia) | 99.73% | L5 | 檢驗異常，無合理機轉 |
| 3 | 先天性無白蛋白血症 (Congenital Analbuminemia) | 99.69% | L5 | 遺傳疾病，抗菌藥無治療機轉 |
| **4** | **淋球菌性尿道炎 (Gonococcal Urethritis)** | 99.59% | **L2** | 抗菌譜涵蓋，有臨床研究（見下） |
| 5 | 尿漿菌尿道炎 (Ureaplasma Urethritis) | 99.59% | L5 | Ureaplasma 無細胞壁，β-內醯胺類理論上無效 |
| 6 | 血型不合 (Blood Group Incompatibility) | 99.59% | L5 | 唯一文獻是關鍵字誤配，無關聯 |
| 7 | 癌前血液系統疾病 | 99.54% | L5 | 無合理機轉 |
| 8 | 會厭炎 (Epiglottitis) | 99.53% | L4 | 抗菌譜涵蓋常見致病菌，但僅有間接文獻 |
| 9 | 單株免疫球蛋白病 (Monoclonal Gammopathy) | 99.50% | L4 | 文獻只談合併感染，未處理疾病本身 |
| 10 | 黃色肉芽腫性腎盂腎炎 | 99.49% | L5 | 抗菌有理，但通常需手術處理，無研究 |

### 淋球菌性尿道炎：臨床試驗

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03867734](https://clinicaltrials.gov/study/NCT03867734) | Phase 2/3 | 完成 | 32 | Aztreonam 用於咽部淋病的示範研究，因應抗藥性淋球菌威脅。部位為咽部而非尿道，樣本小，疑為單臂設計 |

### 淋球菌性尿道炎：文獻

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | 單臂開放性試驗 | Antimicrob Agents Chemother | 單劑 2 g 肌注 Aztreonam 治療淋病的試驗，以重新利用舊抗生素因應頭孢曲松抗藥威脅 |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | 臨床研究 | Antimicrob Agents Chemother | 1 g 肌注 Aztreonam 對比 2 g Spectinomycin，兩組皆無治療失敗，對男性單純尿道淋病療效令人滿意 |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | 臨床研究 | Genitourin Med | 單劑 1 g 肌注治療男性 61 人、女性 26 人，除 1 例咽部外全部清除感染，耐受良好 |
| [6438364](https://pubmed.ncbi.nlm.nih.gov/6438364/) | 1984 | 臨床／細菌學評估 | Jpn J Antibiot | 30 名男性淋菌性尿道炎患者的臨床與細菌學評估，含產青黴素酶菌株 |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | 流行病學與治療研究 | Hinyokika Kiyo | 淋病感染的流行病學與 Aztreonam 單次治療研究 |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | 臨床／微生物學研究 | J Infect Dis | 評估 Aztreonam 對抗青黴素抗藥性淋球菌的效果 |
| [6226596](https://pubmed.ncbi.nlm.nih.gov/6226596/) | 1983 | 臨床研究 | G Ital Dermatol Venereol | 急性淋球菌性尿道炎患者的 Aztreonam 研究（無摘要） |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | 微生物／抗藥性報告 | J Infect Chemother | 出現不產 β-內醯胺酶、對頭孢類及 Aztreonam 高度抗藥的淋球菌，屬抗藥性警訊 |

**綜合判讀：** 這些研究多為 1980 年代的非隨機研究，未顯示優於現行標準療法。屬於同類抗菌藥的延伸，不是機轉上的跳躍。2001 年已有高度抗藥株的報告。較適合針對抗藥性淋病或 β-內醯胺過敏患者提出聚焦的研究問題，不建議直接採用。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68891 | EMBLAVEO POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 1.5G/0.5G（Pfizer Corporation Hong Kong Limited） | — | — |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第 1 的預測（多株性高黏滯症候群）沒有任何臨床或文獻證據，機轉上也沒有合理關聯，只有模型分數，不應推進。
- 前 10 名預測中只有淋球菌性尿道炎（L2、建議為研究問題）有實質證據，但屬非隨機研究，且有抗藥性疑慮。

**若要推進需要：**
- 若聚焦淋球菌性尿道炎：設計針對抗藥性淋病或 β-內醯胺過敏族群的比較性研究，並確認當地淋球菌對 Aztreonam 的藥敏資料。
- 取得香港衛生署仿單的核准適應症、警語與禁忌症。
- 補齊 DrugBank 的作用機轉資料。
- 確認 EMBLAVEO（Aztreonam 與 avibactam 複方）的組成與單方 Aztreonam 證據之間的適用性差異，因為上述研究多以單方 Aztreonam 進行。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

