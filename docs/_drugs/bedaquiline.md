---
layout: default
title: Bedaquiline
parent: 高證據等級 (L1-L2)
nav_order: 85
evidence_level: L2
indication_count: 10
---

# Bedaquiline
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Bedaquiline：從多重抗藥性肺結核到非活動性結核病（潛伏感染預防）

## 一句話總結

Bedaquiline 是全球首個靶向 *Mycobacterium tuberculosis* F-ATP 合成酶的新型抗結核藥，核准用於多重抗藥性肺結核（MDR-TB）治療，在香港尚未取得上市許可。TxGNN 模型對 Bedaquiline 進行 10 項新適應症預測；其中**非活動性結核病 / 潛伏結核預防（Inactive Tuberculosis）**具備最強臨床證據，有 **3 個 Phase 2/3 臨床試驗**（含規模達 2,530 人的 BREACH-TB 試驗）及 **20 篇文獻**支持，建議 **Proceed with Guardrails**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 多重抗藥性結核病（MDR-TB）肺部感染 |
| 最具潛力預測新適應症 | 非活動性結核病 / 潛伏結核預防（Inactive Tuberculosis） |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 十大預測適應症總覽

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議決策 |
|------|--------|-----------|---------|---------|
| 1 | 牛結核病（Tuberculosis, Bovine） | 99.96% | L5 | Hold |
| 2 | 結核性腹水（Tuberculous Ascites） | 99.96% | L4 | Hold |
| **3** | **非活動性結核病（Inactive Tuberculosis）** | **99.96%** | **L2** | **Proceed with Guardrails** |
| 4 | 禽結核病（Tuberculosis, Avian） | 99.96% | L5 | Hold |
| **5** | **結核瘤（Tuberculoma）** | **99.96%** | **L3** | **Research Question** |
| 6 | 外陰陰道念珠菌病（Vulvovaginal Candidiasis） | 99.88% | L5 | Hold ⚠️ |
| 7 | 肝吸蟲病（Fascioliasis） | 99.88% | L5 | Hold ⚠️ |
| 8 | 尿素循環障礙（Urea Cycle Disorder） | 99.78% | L5 | Hold ⚠️ |
| **9** | **皮膚結核（Cutaneous Tuberculosis）** | **99.70%** | **L4** | **Research Question** |
| 10 | 食道念珠菌病（Esophageal Candidiasis） | 99.68% | L5 | Hold ⚠️ |

> ⚠️ 排名 6、7、8、10 為知識圖譜偽陽性：Bedaquiline 對真菌（念珠菌）、多細胞寄生蟲（肝吸蟲）及代謝遺傳疾病（尿素循環障礙）無任何已知靶點或生物學機制連結，應予排除。

---

## 主要預測一：非活動性結核病（Inactive Tuberculosis）— L2，Proceed with Guardrails

### 為什麼這個預測合理？

Bedaquiline 的作用靶點是 *M. tuberculosis* **F₁F₀-ATP 合成酶次單元 c**，直接阻斷細菌氧化磷酸化能量生成。這個機轉的關鍵特性是：即使在**代謝靜止或低複製速率的菌體**（dormant/non-replicating bacilli）中，ATP 合成酶仍維持基礎活性以維持膜電位——使 Bedaquiline 對潛伏菌體同樣具備殺菌效力。相較之下，傳統一線藥物（如異菸鹼醯胺 INH）對靜止期菌體的效力顯著下降。

非活動性結核病與潛伏結核感染（LTBI）正是 *M. tuberculosis* 低代謝活性的典型情境，與 Bedaquiline 機轉最契合。全球約四分之一人口帶有潛伏感染，其中 5–10% 終生有再活化風險，預防性治療（TPT）需求龐大。

目前已有 Phase 2/3 試驗 **BREACH-TB（NCT06568484）**直接評估 Bedaquiline 用於 HIV 感染者及 MDR-TB 接觸者的結核預防，招募規模 2,530 人，預計 2027 年完成——這是 TPT 領域最直接的臨床證據。此外，2022 年動物研究（PMID 34939891）已證明長效注射型 Bedaquiline 在小鼠預防療法模型中注射後活性可維持最多 12 週，為提升療程依從性提供了潛力基礎。

### 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06568484](https://clinicaltrials.gov/study/NCT06568484) | Phase 2/3 | 尚未開始招募 | 2,530 | BREACH-TB：4 週 Bedaquiline 對比標準方案，預防 HIV 感染者及 DS/RR-TB 接觸者發病；72 週追蹤，直接針對潛伏/非活動性結核預防情境，規模最大 |
| [NCT05766267](https://clinicaltrials.gov/study/NCT05766267) | Phase 2/3 | 進行中（不再招募） | 288 | CRUSH-TB：含 Bedaquiline 的 17 週短程肺結核方案（BMZ + Rifabutin 或 Delamanid）對比標準 6 個月療程；對靜止菌體清除評估具間接意義 |
| [NCT07069582](https://clinicaltrials.gov/study/NCT07069582) | Phase 1 | 尚未開始招募 | 60 | SSTARLET 子研究：評估哺乳期婦女 Bedaquiline 血漿及母乳 PK，補充特殊族群安全性資料 |

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33837535](https://pubmed.ncbi.nlm.nih.gov/33837535/) | 2021 | Systematic Review / Guideline | Clin Pharmacol Ther | 結核病治療完整指引；涵蓋潛伏 vs 活動性 TB 的早期殺菌活性與滅菌活性機轉差異，確立 Bedaquiline 的靜止菌體殺菌地位 |
| [39887565](https://pubmed.ncbi.nlm.nih.gov/39887565/) | 2025 | Review | Respirology | 2025 TB 臨床更新：TB 為連續疾病譜而非二元分類，亞臨床 TB 傳播被低估；Bedaquiline 收入新型縮短療程方案 |
| [39766559](https://pubmed.ncbi.nlm.nih.gov/39766559/) | 2024 | Review | Antibiotics (Basel) | F-ATP 合成酶靶點詳細分子機轉；解釋 Bedaquiline 在休眠菌體中維持活性的電化學梯度依賴機制 |
| [34939891](https://pubmed.ncbi.nlm.nih.gov/34939891/) | 2022 | Animal Study | Am J Respir Crit Care Med | 長效注射型 Bedaquiline 在小鼠預防療法模型驗證；單次注射活性維持最多 12 週，有潛力大幅改善 TPT 依從性 |
| [39301910](https://pubmed.ncbi.nlm.nih.gov/39301910/) | 2025 | Review | Infect Disord Drug Targets | Bedaquiline 創新遞藥系統；明確指出其可靶向潛伏/靜止型 TB 菌體，為傳統藥物難以企及的優勢 |
| [36915977](https://pubmed.ncbi.nlm.nih.gov/36915977/) | 2022 | Review | J Zhejiang Univ Med Sci | 潛伏結核診斷與治療進展；全球四分之一人口感染 LTBI，現有 TST/IGRA 診斷局限性及新型生物標記探討 |
| [36982277](https://pubmed.ncbi.nlm.nih.gov/36982277/) | 2023 | Review | Int J Mol Sci | TB 病理機制與新藥靶點全面回顧；含 Bedaquiline ATP 合成酶抑制機轉說明及耐藥分枝桿菌的治療挑戰 |
| [28625141](https://pubmed.ncbi.nlm.nih.gov/28625141/) | 2018 | Review | Recent Pat Anti Infect Drug Discov | Bedaquiline 專論：從發現到核准的歷程、臨床試驗數據及縮短 MDR-TB 療程的新希望 |
| [29580819](https://pubmed.ncbi.nlm.nih.gov/29580819/) | 2018 | Review | Lancet Infect Dis | 結核病新藥、新療程及宿主導向治療進展；Bedaquiline 作為主要突破性藥物，MDR-TB 存活率改善 |
| [29187395](https://pubmed.ncbi.nlm.nih.gov/29187395/) | 2018 | Review | Clin Microbiol Rev | 休眠狀態 *M. tuberculosis* 的新治療策略；Bedaquiline 對非複製菌體的活性詳細分析 |

---

## 其他值得關注的預測

### 結核瘤（Tuberculoma）— 排名 5，L3，Research Question

#### 為什麼值得關注？

結核瘤為 *M. tuberculosis* 在中樞神經系統形成的肉芽腫性病灶，屬肺外結核的嚴重類型。多份案例報告記錄 Bedaquiline 在 BPaL 方案（Bedaquiline + Pretomanid + Linezolid）中成功治療 MDR/XDR-TB 相關 CNS 病灶，顯示其血腦屏障穿透能力。目前缺乏前瞻性臨床試驗，為純觀察性/案例研究支持（L3）。

#### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34876446](https://pubmed.ncbi.nlm.nih.gov/34876446/) | 2021 | Case Report | BMJ Case Reports | XDR-TB 患者接受 BPaL 方案治療後形成**無菌結核瘤**（Nix-TB 試驗相關）；首次記錄 Bedaquiline 於 CNS 結核瘤的直接臨床應用 |
| [40817574](https://pubmed.ncbi.nlm.nih.gov/40817574/) | 2025 | Case Report | Am J Case Reports | MDR-TB 伴結核性腦膜炎成功治療；強調 CNS 穿透藥物選擇的重要性 |
| [31720380](https://pubmed.ncbi.nlm.nih.gov/31720380/) | 2018 | Case Report | J Clin Tuberc Other Mycobact Dis | 播散性 MDR-TB 伴 CNS 結核瘤；含 Bedaquiline 的救治方案討論 |
| [33400226](https://pubmed.ncbi.nlm.nih.gov/33400226/) | 2021 | Review | Acta Neurol Belgica | 神經結核全面更新；結核性腦膜炎佔神經結核 70–80%，兒童結核瘤多見於小腦 |

---

### 皮膚結核（Cutaneous Tuberculosis）— 排名 9，L4，Research Question

#### 為什麼值得關注？

皮膚結核為 *M. tuberculosis* 感染皮膚的肺外結核類型。Phase 3 BEEP 試驗（NCT05597280，n=124,000）評估 Bedaquiline 用於麻瘋病（*M. leprae*）接觸者預防，間接支持其對皮膚分枝桿菌感染的跨物種活性潛力。

> **注意**：現有 2 篇相關文獻均為抗結核藥物引起的**皮膚不良反應**案例，並非皮膚結核的療效文獻，不可混淆。

#### 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05597280](https://clinicaltrials.gov/study/NCT05597280) | Phase 3 | 招募中 | 124,000 | BEEP 試驗：Bedaquiline 強化麻瘋病接觸者預防（BE-PEP）對比標準 Rifampicin 單劑預防；間接支持跨分枝桿菌屬廣譜活性，不可直接外推至皮膚結核療效 |

---

### 不建議推進的預測（偽陽性或臨床需求極低）

| 適應症 | 排名 | 排除理由 |
|--------|------|---------|
| 牛結核病（*M. bovis*） | 1 | 人獸共患管控議題，人體治療需求極低；ATP 合成酶靶點雖與 *M. tuberculosis* 同源，但無任何人類臨床試驗或文獻 |
| 結核性腹水 | 2 | 同源病原菌間接推論，無任何臨床試驗或文獻直接支持 |
| 禽結核病（*M. avium*） | 4 | 不同菌種，體外 MIC 差異顯著；TxGNN 高分反映知識圖譜「結核相關」節點鄰近性而非生物活性 |
| 外陰陰道念珠菌病 | 6 | 真菌 ATP 合成酶結構與細菌差異極大，無任何已知機轉連結；知識圖譜偽陽性 |
| 肝吸蟲病 | 7 | 多細胞寄生蟲，線粒體 ATP 合成酶與細菌型差異極大；無任何支持性機制或證據 |
| 尿素循環障礙 | 8 | 先天性代謝遺傳疾病，與感染無關；Bedaquiline 無任何代謝酵素調節機制，屬知識圖譜遠距假訊號 |
| 食道念珠菌病 | 10 | 同外陰陰道念珠菌病；Bedaquiline 對真菌無已知靶點 |

---

## 香港上市資訊

Bedaquiline 在香港目前**未取得上市許可**，無任何藥品許可證（共 0 張）。如需在香港使用，須透過特殊用藥途徑（如特別申請或恩慈用藥機制）取得。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意**：本 Evidence Pack 標記 TFDA 仿單警語/禁忌（DG001）及作用機轉（DG002）均為資料缺口（Data Gap），屬**封鎖性（Blocking）**及高嚴重性缺口，進入正式安全性評估前須優先補足。

---

## 結論與下一步

**決策：Proceed with Guardrails（針對非活動性結核病 / 潛伏結核預防）**

**理由：**
BREACH-TB（NCT06568484）是目前規模最大的 Bedaquiline 預防用途 Phase 2/3 試驗（n=2,530），直接評估潛伏/非活動性結核預防情境；Bedaquiline 對代謝靜止菌體的獨特 ATP 合成酶抑制機轉，以及長效製劑動物模型的有效性，共同支持其臨床轉譯可行性，證據等級達 L2。

**若要推進需要：**
- 補充完整 MOA 資料（DG002，透過 DrugBank API 查詢，目前為 High 嚴重性缺口）
- 取得原廠仿單警語與禁忌症資料（DG001，Blocking 嚴重性缺口，影響安全性初評）
- 追蹤 BREACH-TB 試驗進展（預計 2027 年 9 月完成）及其期中分析結果
- 完善藥物交互作用（DDI）資料（目前查詢無結果，需擴大查詢範圍）
- 規劃香港上市許可路徑（目前 0 張許可證，需完整法規策略）
- 結核瘤及皮膚結核可列為獨立研究問題，設計前瞻性觀察性研究或病例系列

---

> **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。所有老藥新用候選適應症均需經過嚴格臨床驗證才能應用於實際患者照護。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

