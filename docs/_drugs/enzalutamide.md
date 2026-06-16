---
layout: default
title: Enzalutamide
parent: 高證據等級 (L1-L2)
nav_order: 273
evidence_level: L1
indication_count: 7
---

# Enzalutamide
{: .fs-9 }

證據等級: **L1** | 預測適應症: **7** 個
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

# Enzalutamide：從去勢抵抗性攝護腺癌到男性生殖器官癌 (Male Reproductive Organ Cancer)

## 一句話總結

Enzalutamide 是第二代雄激素受體（AR）拮抗劑，全球已核准用於轉移性去勢抵抗性攝護腺癌（mCRPC）、非轉移性去勢抵抗性攝護腺癌（nmCRPC）及轉移性去勢敏感性攝護腺癌（mCSPC），但目前香港尚無正式許可登記。
TxGNN 模型預測其對**男性生殖器官癌 (Male Reproductive Organ Cancer)** 具有高度療效，預測分數達 **99.51%**，目前有 **50 個臨床試驗**和 **20 篇文獻**支持此預測方向，為本評估各預測適應症中最具臨床實證的方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 攝護腺癌（全球核准，香港未正式登記） |
| 預測新適應症 | 男性生殖器官癌 (Male Reproductive Organ Cancer) |
| TxGNN 預測分數 | 99.51% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Enzalutamide 透過三重機轉全面封鎖雄激素訊號軸：①競爭性抑制 DHT 與雄激素受體（AR）的高親和力結合（親和力約為 bicalutamide 的 5–8 倍）；②阻斷 AR 由細胞質向細胞核的核轉位；③直接抑制 AR 與 DNA 的結合及下游轉錄活化。此多重阻斷機轉有效避免第一代抗雄激素藥物常見的「拮抗劑轉促效劑（agonist switch）」問題。

男性生殖器官癌以攝護腺癌為絕對主體，而攝護腺癌本質上是雄激素驅動腫瘤，AR 訊號軸為其核心致癌驅力。因此 TxGNN 模型的此預測，實質上對應了 Enzalutamide 全球已確立的 **on-target 核心適應症**。迄今已完成 AFFIRM（化療後 mCRPC）、PREVAIL（化療前 mCRPC）、PROSPER（nmCRPC）、ARCHES（mCSPC）、EMBARK（高風險非轉移 CSPC）等多個大型 Phase 3 隨機對照試驗，涵蓋攝護腺癌全病程，確立其療效地位。

值得注意的是，TxGNN 亦對攝護腺相關良性腫瘤（如 prostate leiomyoma、fibroma of prostate、benign prostate phyllodes tumor）、卵巢 Brenner 腫瘤及攝護腺癌/腦癌遺傳易感性等適應症做出預測，但上述預測均缺乏任何臨床試驗或文獻支持（證據等級 L5，建議 Hold），不建議列為優先推進方向。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01212991](https://clinicaltrials.gov/study/NCT01212991) | Phase 3 | 完成 | 1,717 | PREVAIL：化療前 mCRPC，Enzalutamide vs 安慰劑，顯著改善整體存活（OS）及影像學無進展存活（rPFS），為 FDA 化療前 mCRPC 核准的關鍵試驗 |
| [NCT02003924](https://clinicaltrials.gov/study/NCT02003924) | Phase 3 | 完成 | 1,401 | PROSPER：nmCRPC 患者（PSA 倍增時間 ≤10 個月），Enzalutamide 顯著延長轉移游離存活期（MFS），支持 nmCRPC 適應症核准 |
| [NCT06551324](https://clinicaltrials.gov/study/NCT06551324) | Phase 3 | 招募中 | 600 | MEVPRO-1：Mevrometostat（EZH2/1 抑制劑）+ Enzalutamide 對比 Enzalutamide 或 Docetaxel 用於 Abiraterone 失敗後 mCRPC，設計確認 Enzalutamide 為標準治療骨幹 |
| [NCT01949337](https://clinicaltrials.gov/study/NCT01949337) | Phase 3 | 未知 | 1,311 | Enzalutamide 單臂 vs Enzalutamide + Abiraterone + Prednisone 三合一治療去勢抵抗性轉移性攝護腺癌的直接頭對頭比較 |
| [NCT00268476](https://clinicaltrials.gov/study/NCT00268476) | Phase 2/3 | 進行中（停止招募） | 11,992 | STAMPEDE：2005 年啟動之多臂多階段平台試驗，評估多種新型療法加入標準 ADT，為攝護腺癌最大規模平台試驗 |
| [NCT02057939](https://clinicaltrials.gov/study/NCT02057939) | Phase 2 | 完成 | 38 | STREAM：Enzalutamide + ADT 聯合拯救性放射治療用於術後 PSA 復發（0.2–4 ng/mL），評估 2 年無進展存活率 |
| [NCT03338790](https://clinicaltrials.gov/study/NCT03338790) | Phase 2 | 完成 | 292 | Nivolumab 聯合 Enzalutamide、Rucaparib 或 Docetaxel 用於去勢抵抗性轉移性攝護腺癌，三臂安全性與療效評估 |
| [NCT03103724](https://clinicaltrials.gov/study/NCT03103724) | Phase 2 | 完成 | 68 | 單臂多中心研究，評估 Enzalutamide 在具至少一個內臟器官轉移之 mCRPC 患者的 3 個月疾病控制率（DCR）及 AR-V7 的預測價值 |
| [NCT02799745](https://clinicaltrials.gov/study/NCT02799745) | Phase 2 | 完成 | 227 | ENACT：Enzalutamide 用於接受主動監測之局限性攝護腺癌患者，隨機比較病理或治療性疾病進展時間 |
| [NCT01981122](https://clinicaltrials.gov/study/NCT01981122) | Phase 2 | 完成 | 52 | 隨機研究比較 Sipuleucel-T 與 Enzalutamide 同步 vs 序貫給藥在 mCRPC 的療效，評估免疫療法與 AR 拮抗劑的最佳治療時序 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28655021](https://pubmed.ncbi.nlm.nih.gov/28655021/) | 2017 | 系統回顧 | JAMA | 攝護腺癌診斷與治療全面回顧，確立 Enzalutamide 等新型 AR 拮抗劑在進展性攝護腺癌的核心角色 |
| [32534790](https://pubmed.ncbi.nlm.nih.gov/32534790/) | 2020 | Review | Trends in Cancer | 進展期攝護腺癌治療格局演進綜述，Enzalutamide 等 ARPI 藥物的適應症選擇、序列治療及療效比較 |
| [29460922](https://pubmed.ncbi.nlm.nih.gov/29460922/) | 2018 | Review | Nature Reviews Urology | Enzalutamide/Abiraterone 耐藥後神經內分泌表型轉變與細胞可塑性機制，揭示 AR 非依賴性耐藥通路 |
| [31614208](https://pubmed.ncbi.nlm.nih.gov/31614208/) | 2020 | Review | J Steroid Biochem Mol Biol | 攝護腺組織（良性與惡性）中雄激素旁分泌合成（intracrinology）回顧，解釋 AR 訊號在去勢後持續驅動腫瘤的生化機制 |
| [34752846](https://pubmed.ncbi.nlm.nih.gov/34752846/) | 2022 | 轉譯研究 | Cancer Letters | 骨轉移微環境中 Enzalutamide 誘導 PTH1R 介導之 TGFBR2 降解，解析約半數骨轉移患者 Enzalutamide 耐藥的微環境機制 |
| [32989253](https://pubmed.ncbi.nlm.nih.gov/32989253/) | 2020 | 生物標記研究 | Oncogene | AR-V7 剪接變體作為 Enzalutamide 及 Abiraterone 耐藥的功能性驅動因子（非僅為被動標記），直接影響序列治療選擇 |
| [37844613](https://pubmed.ncbi.nlm.nih.gov/37844613/) | 2023 | 機轉/前臨床 | Nature | 抑制骨髓細胞趨化可逆轉部分攝護腺癌的 Enzalutamide 耐藥，揭示腫瘤免疫微環境在耐藥中的新角色 |
| [34489465](https://pubmed.ncbi.nlm.nih.gov/34489465/) | 2021 | 單細胞基因組 | Nature Communications | 單細胞 ATAC/RNA 定序鑑別 Enzalutamide 治療前已存在及治療後持續的細胞亞群，定義耐藥前驅細胞的染色質特徵 |
| [33483372](https://pubmed.ncbi.nlm.nih.gov/33483372/) | 2021 | 前臨床 | Cancer Research | Ferroptosis 誘導劑（鐵依賴性氧化性細胞死亡）在進展性攝護腺癌及 Enzalutamide 耐藥模型中的新型治療潛力 |
| [32355025](https://pubmed.ncbi.nlm.nih.gov/32355025/) | 2020 | 單細胞基因組 | Science | 攝護腺腔細胞再生潛力的單細胞分析，雄激素剝奪後 Sca1⁺/Psca⁺ 幹樣細胞群在腺體縮退與再生中的機轉 |

---

## 香港上市資訊

Enzalutamide 目前在香港未取得任何藥劑產品許可證，無核准適應症登記。如需引進，須向衞生署藥物辦公室申請正式藥劑產品登記，可引用以下國際監管核准作為橋接依據：

| 監管機構 | 核准適應症範疇 | 首次核准年份 |
|---------|-------------|------------|
| 美國 FDA | mCRPC（化療後/前）、nmCRPC、mCSPC | 2012–2019 |
| 歐洲 EMA | mCRPC、nmCRPC、mCSPC | 2013 年起 |
| 日本 PMDA | 去勢抵抗性攝護腺癌 | 2014 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（雄激素受體信號通路抑制劑，ARPI），**非**傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 低（不具直接骨髓毒性；臨床試驗中偶見輕度嗜中性白血球減少，非主要毒性） |
| 致吐性分級 | 低度（口服劑型，致吐風險極低） |
| 監測項目 | 肝功能（ALT/AST/Bilirubin）、血壓、CBC（含分類）、癲癇發作風險評估、認知功能監測 |
| 處置防護 | 無需特殊細胞毒性藥物防護設備；建議孕婦避免接觸；依一般口服抗癌藥物規範處置 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Enzalutamide 在全球多個大型 Phase 3 RCT（PREVAIL n=1,717、PROSPER n=1,401、STAMPEDE n=11,992 等）中確立了對攝護腺癌（男性生殖器官癌）的療效，TxGNN 預測分數達 99.51%，對應 L1 最高證據等級。香港目前雖無正式許可，但美國 FDA、歐洲 EMA、日本 PMDA 均已核准，具備充分的全球監管與科學依據支持引進評估。

**若要推進需要：**
- **安全性文件**：取得 Xtandi® 完整仿單，補充警語（特別是癲癇發作風險）、禁忌症及藥物交互作用資料（目前為 Data Gap）
- **作用機轉資料**：透過 DrugBank API 補充完整 MOA 及毒理學資訊（目前為 Data Gap）
- **香港登記申請**：準備衞生署藥物辦公室藥劑產品登記所需文件，利用 FDA/EMA 核准資料作橋接依據
- **亞裔族群數據**：評估亞裔（尤其華人）族群的藥效學與安全性差異，特別是 HSD3B1 基因多態性對療效的影響
- **風險管理計劃**：針對癲癇高風險患者、高齡患者（>75 歲）及心血管風險族群制定個別化監測方案
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

